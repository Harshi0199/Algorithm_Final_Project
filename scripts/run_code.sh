#!/bin/bash

# Function to calculate memory usage in MB*seconds
calculate_memory_usage() {
    local dat_file=$1
    awk 'BEGIN { 
        prev_time = 0; 
        prev_mem_mb = 0; 
        mem_time_mb_s = 0;
    }
    NR>1 {
        mem_in_mb = $2;
        timestamp = $3;
        
        if (prev_time > 0) {
            time_interval_s = timestamp - prev_time;
            mem_time_mb_s += (prev_mem_mb + mem_in_mb) / 2 * time_interval_s;
        }
        
        prev_time = timestamp;
        prev_mem_mb = mem_in_mb;
    }
    END {
        printf "%.2f\n", mem_time_mb_s;
    }' "$dat_file"
}

folder_path="$1"
max_execution_time="$2"

# Check if folder path exists
if [ ! -d "$folder_path" ]; then
    echo "Error: Folder path does not exist."
    exit 1
fi

# Loop through each .py file in the folder
for completion_file in "$folder_path"/*.py; do
    completion_dat_file="${completion_file%.py}.dat"
    echo "Executing $completion_file"

    error_output=$(mktemp)
    
    start_time=$(gdate +%s)
    start_ms=$(gdate +%3N)
    start_time_ms=$((10#$start_time * 1000 + 10#$start_ms))



   
    rm -f "$completion_dat_file"
    
    # Run the Python script with memory profiling
    timeout "$max_execution_time" mprof run --interval 0.001 --output "$completion_dat_file" python3 "$completion_file" 2> "$error_output"
    end_time=$(gdate +%s)
    end_ms=$(gdate +%3N)
    end_time_ms=$((10#$end_time * 1000 + 10#$end_ms))
    execution_time=$((end_time_ms - start_time_ms))

    exit_status=$?

    # Check execution status
    echo "Execution status for $completion_file: $exit_status"
    if [ $exit_status -ne 0 ]; then
        echo "❌ Execution failed for $completion_file. Removing .dat file."
        rm -f "$completion_dat_file"
    elif [ ! -f "$completion_dat_file" ]; then
        echo "⚠️ Execution completed but no .dat file found for $completion_file."
    else
        if [ -s "$error_output" ]; then
            echo "⚠️ Non-empty stderr detected (may be harmless):"
            cat "$error_output"
        fi
        mem_usage_mb_s=$(calculate_memory_usage "$completion_dat_file")
        echo "✅ Memory usage (MB*seconds): $mem_usage_mb_s"
    fi


    # Clean up
    rm -f "$error_output"
done

#!/bin/bash

calculate_memory_metrics() {
    local dat_file=$1
    awk 'BEGIN {
        prev_time = 0;
        prev_mem = 0;
        mem_sec = 0;
        max_mem = 0;
        sum_mem = 0;
        count = 0;
    }
    NR > 1 {
        mem = $2; time = $3;
        if (prev_time > 0) {
            dt = time - prev_time;
            mem_sec += (prev_mem + mem) / 2 * dt;
        }
        if (mem > max_mem) max_mem = mem;
        sum_mem += mem; count++;
        prev_time = time; prev_mem = mem;
    }
    END {
        avg = (count > 0) ? sum_mem / count : 0;
        printf "%.2f %.2f %.2f", mem_sec, avg, max_mem;
    }' "$dat_file"
}

check_mprof() {
    if ! command -v mprof &> /dev/null; then
        echo "Installing memory_profiler..."
        pip install memory_profiler || { echo "Failed to install memory_profiler"; exit 1; }
    fi
}

check_mprof

# Inputs
dat_root="$1"
py_root="$2"
csv_output="${3:-combined_metrics.csv}"
excel_output="${4:-combined_metrics.xlsx}"
timeout_secs=30

if [ ! -d "$dat_root" ] || [ ! -d "$py_root" ]; then
    echo "Usage: $0 <dat_results_root> <python_programs_root> [csv_output.csv] [excel_output.xlsx]"
    exit 1
fi

# Temp file for raw metrics
raw_metrics_file="raw_metrics.tmp"
> "$raw_metrics_file"

# Process all .dat files
find "$dat_root" -type f -name "*.dat" | while read -r dat_file; do
    relative_path="${dat_file#$dat_root/}"
    source_dir=$(echo "$relative_path" | cut -d'/' -f1) # Gemini, Claude, etc.
    dir_name=$(dirname "$relative_path")
    base_name=$(basename "$dat_file" .dat)
    py_file="$py_root/$dir_name/$base_name.py"

    if [ ! -f "$py_file" ]; then
        echo "Warning: No matching Python file for $dat_file"
        continue
    fi

    echo "Processing $relative_path"

    # Run Python script and measure execution time
    read -r execution_time status <<<$(python3 - <<EOF
import subprocess, time

start_ns = time.perf_counter_ns()
try:
    result = subprocess.run(['python3', '$py_file', '--skip-tests'], capture_output=True, text=True, timeout=$timeout_secs)
    return_code = result.returncode
except Exception:
    return_code = -1
end_ns = time.perf_counter_ns()
exec_time_ms = (end_ns - start_ns) / 1_000_000
print(f"{exec_time_ms} {return_code}")
EOF
)

    if [ -s "$dat_file" ]; then
        metrics=$(calculate_memory_metrics "$dat_file")
        mem_usage_mb_s=$(echo "$metrics" | cut -d' ' -f1)
        avg_mem_mb=$(echo "$metrics" | cut -d' ' -f2)
        max_mem_mb=$(echo "$metrics" | cut -d' ' -f3)
    else
        mem_usage_mb_s=0; avg_mem_mb=0; max_mem_mb=0
    fi

    # Write to temp file
    printf "%s,%s,%.3f,%.3f,%.3f,%.3f\n" "$base_name.py" "$source_dir" "$execution_time" "$mem_usage_mb_s" "$avg_mem_mb" "$max_mem_mb" >> "$raw_metrics_file"
done

# Final aggregation and Excel writing with chart
# Final step: call external Python script to generate Excel with charts
python3 performance_metrics/generate_excel_with_chart.py "$raw_metrics_file" "$excel_output"

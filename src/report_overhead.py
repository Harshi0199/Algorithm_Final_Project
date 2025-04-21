import json
import os
import glob
import argparse

def calculate_memory_usage(dat_file_path):
    with open(dat_file_path, 'r') as file:
        prev_time = 0
        prev_mem_mb = 0
        mem_time_mb_s = 0
        next(file)
        for line in file:
            if "__main__." in line:
                continue
            parts = line.split()
            mem_in_mb = float(parts[1])
            timestamp = float(parts[2])
            if prev_time > 0:
                time_interval_s = timestamp - prev_time
                mem_time_mb_s += (prev_mem_mb + mem_in_mb) / 2 * time_interval_s
            prev_time = timestamp
            prev_mem_mb = mem_in_mb
        return mem_time_mb_s

def calculate_runtime(dat_file_path):
    with open(dat_file_path, 'r') as file:
        start_time = float("inf")
        end_time = float("-inf")
        next(file)
        for line in file:
            if "__main__." in line:
                continue
            parts = line.split()
            timestamp = float(parts[2])
            start_time = min(start_time, timestamp)
            end_time = max(end_time, timestamp)
        return max(end_time - start_time, 0)

def report_max_memory_usage(dat_file_path):
    max_memory_usage = 0
    with open(dat_file_path, 'r') as file:
        next(file)
        for line in file:
            if "__main__." in line:
                continue
            parts = line.split()
            mem_in_mb = float(parts[1])
            max_memory_usage = max(max_memory_usage, mem_in_mb)
        return max_memory_usage

# 🎯 Parse input arguments
parser = argparse.ArgumentParser(description="Memory & Performance Report Generator")
parser.add_argument('--canonical_dir', required=True, help='Path to canonical solution .dat files')
parser.add_argument('--model_dirs', nargs='+', required=True, help='Paths to model .dat files (space-separated)')
parser.add_argument('--model_names', nargs='+', required=True, help='Model names for labeling output (space-separated)')
args = parser.parse_args()

# 🧠 Read canonical results
canonical_solution_memory_usage = {}
canonical_solution_execution_time = {}
canonical_solution_max_memory_usage = {}

for dat_file in glob.glob(os.path.join(args.canonical_dir, "*.dat")):
    try:
        problem_idx = os.path.basename(dat_file).split('.')[0]
        canonical_solution_memory_usage[problem_idx] = calculate_memory_usage(dat_file)
        canonical_solution_execution_time[problem_idx] = calculate_runtime(dat_file)
        canonical_solution_max_memory_usage[problem_idx] = report_max_memory_usage(dat_file)
    except:
        pass

# 🔁 Iterate over models
for model, dat_directory in zip(args.model_names, args.model_dirs):
    completion_memory_usage = {}
    execution_time = {}
    max_memory_usage = {}
    task_idx = {}

    for dat_file in glob.glob(os.path.join(dat_directory, "*.dat")):
        try:
            problem_idx = os.path.basename(dat_file).split('.')[0]
            completion_memory_usage[problem_idx] = calculate_memory_usage(dat_file)
            execution_time[problem_idx] = calculate_runtime(dat_file)
            max_memory_usage[problem_idx] = report_max_memory_usage(dat_file)
            task_idx[problem_idx] = dat_file

        except Exception as e:
            print(f"❌ Error processing {dat_file}: {e}")

    # 🧮 Metrics
    total_execution_time = 0
    normalized_execution_time = 0
    total_max_memory_usage = 0
    normalized_max_memory_usage = 0
    total_memory_usage = 0
    total_canonical_solution_max_memory_usage = 0
    total_canonical_solution_execution_time = 0
    total_canonical_solution_memory_usage = 0
    normalized_memory_usage = 0
    total_codes = 0
    normalized_execution_time_list = []
    normalized_max_memory_usage_list = []
    normalized_memory_usage_list = []

    for idx in completion_memory_usage.keys():
        if idx not in canonical_solution_memory_usage:
            continue

    # calculations continue as before...


        total_memory_usage += completion_memory_usage[idx]
        total_execution_time += execution_time[idx]
        total_max_memory_usage += max_memory_usage[idx]
        total_canonical_solution_max_memory_usage += canonical_solution_max_memory_usage[idx]
        total_canonical_solution_memory_usage += canonical_solution_memory_usage[idx]
        total_canonical_solution_execution_time += canonical_solution_execution_time[idx]

        normalized_execution_time += execution_time[idx] / canonical_solution_execution_time[idx]
        normalized_execution_time_list.append(execution_time[idx] / canonical_solution_execution_time[idx])

        normalized_max_memory_usage += max_memory_usage[idx] / canonical_solution_max_memory_usage[idx]
        normalized_max_memory_usage_list.append(max_memory_usage[idx] / canonical_solution_max_memory_usage[idx])

        normalized_memory_usage += completion_memory_usage[idx] / canonical_solution_memory_usage[idx]
        normalized_memory_usage_list.append(completion_memory_usage[idx] / canonical_solution_memory_usage[idx])

        total_codes += 1

    if total_codes == 0:
        print(f"⚠️ Skipping empty model results: {model}")
        continue

    normalized_execution_time = total_execution_time / total_canonical_solution_execution_time
    normalized_max_memory_usage = total_max_memory_usage / total_canonical_solution_max_memory_usage
    normalized_memory_usage = total_memory_usage / total_canonical_solution_memory_usage
    total_execution_time = total_execution_time / total_codes
    total_memory_usage = total_memory_usage / total_codes
    total_max_memory_usage = total_max_memory_usage / total_codes

    # 📦 Save output
    output_json = {
        "model": model,
        "total_codes": total_codes,
        "average_execution_time_sec": round(total_execution_time, 2),
        "normalized_execution_time": round(normalized_execution_time, 2),
        "average_max_memory_usage_mb": round(total_max_memory_usage, 2),
        "normalized_max_memory_usage": round(normalized_max_memory_usage, 2),
        "average_memory_usage_mb_s": round(total_memory_usage, 2),
        "normalized_memory_usage": round(normalized_memory_usage, 2)
    }

    with open(f"{model}_performance_summary.json", "w") as f:
        json.dump(output_json, f, indent=4)

    # 🖨️ Table row print
    print(f"\n{model}&{total_execution_time:.2f}&{normalized_execution_time:.2f}&{total_max_memory_usage:.2f}&{normalized_max_memory_usage:.2f}&{total_memory_usage:.2f}&{normalized_memory_usage:.2f}\\\\")
    print(f"✅ JSON saved to {model}_performance_summary.json")

"""
This script compares multiple Python solutions across four folders:
    Folders:
       - generated_solutions
       - ChatGPT
       - Gemini
       - Claude

For each task, the same problem is implemented in different folders. For example:
  Task: lexicographically_smallest_string_after_substring_operation
       - generated_solutions/lexicographically_smallest_string_after_substring_operation.py
       - ChatGPT/lexicographically_smallest_string_after_substring_operation_chatgpt.py
       - Gemini/lexicographically_smallest_string_after_substring_operation_gemini.py
       - Claude/lexicographically_smallest_string_after_substring_operation_claude.py

  Task: advantage_shuffle
       - generated_solutions/advantage_shuffle.py
       - ChatGPT/advantage_shuffle_chatgpt.py
       - Gemini/advantage_shuffle_gemini.py
       - Claude/advantage_shuffle_claude.py

  Task: maximum_strength_of_a_group
       - generated_solutions/maximum_strength_of_a_group.py
       - ChatGPT/maximum_strength_of_a_group_chatgpt.py
       - Gemini/maximum_strength_of_a_group_gemini.py
       - Claude/maximum_strength_of_a_group_claude.py

Each file is executed concurrently with a timeout (10 seconds), and a return code of 0 is considered a Pass.
The results are summarized via a grouped bar chart (aggregated across tasks) and an HTML report
with a table showing each task's Pass/Fail results for each folder.
"""

import os
import subprocess
import concurrent.futures

# Force matplotlib to use the 'Agg' backend so we can save charts without a display.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def run_script(filepath):
    """
    Executes a Python file and returns a tuple:
      (filepath, return_code, stdout, stderr).
    A return code of 0 indicates a pass; otherwise, a failure.
    """
    try:
        result = subprocess.run(
            ["python", filepath],
            capture_output=True,
            text=True,
            timeout=10
        )
        return (filepath, result.returncode, result.stdout, result.stderr)
    except Exception as e:
        # Treat any exception (timeout, etc.) as a failure with returncode -1.
        return (filepath, -1, "", str(e))

def main():
    # List of tasks. Each task is represented as a dictionary.
    # Each task contains the problem name and the expected file name (per folder).
    # You can add more tasks in the same format.
    tasks = [
        {
            "problem_name": "lexicographically_smallest_string_after_substring_operation",
            "generated_solutions": "lexicographically_smallest_string_after_substring_operation.py",
            "ChatGPT": "lexicographically_smallest_string_after_substring_operation_chatgpt.py",
            "Gemini": "lexicographically_smallest_string_after_substring_operation_gemini.py",
            "Claude": "lexicographically_smallest_string_after_substring_operation_claude.py"
        },
        {
            "problem_name": "advantage_shuffle",
            "generated_solutions": "advantage_shuffle.py",
            "ChatGPT": "advantage_shuffle_chatgpt.py",
            "Gemini": "advantage_shuffle_gemini.py",
            "Claude": "advantage_shuffle_claude.py"
        },
        {
            "problem_name": "maximum_strength_of_a_group",
            "generated_solutions": "maximum_strength_of_a_group.py",
            "ChatGPT": "maximum_strength_of_a_group_chatgpt.py",
            "Gemini": "maximum_strength_of_a_group_gemini.py",
            "Claude": "maximum_strength_of_a_group_claude.py"
        },
        {
           "problem_name": "maximum_running_time_of_n_computers",
            "generated_solutions": "maximum_running_time_of_n_computers.py",
            "ChatGPT": "maximum_running_time_of_n_computers_chatgpt.py",
            "Gemini": "maximum_running_time_of_n_computers_gemini.py",
            "Claude": "maximum_running_time_of_n_computers_claude.py" 
        },
        {
           "problem_name": "maximum_strength_of_a_group",
            "generated_solutions": "maximum_strength_of_a_group.py",
            "ChatGPT": "maximum_strength_of_a_group_chatgpt.py",
            "Gemini": "maximum_strength_of_a_group_gemini.py",
            "Claude": "maximum_strength_of_a_group_claude.py" 
        },
        {
           "problem_name": "maximum_total_beauty_of_the_gardens",
            "generated_solutions": "maximum_total_beauty_of_the_gardens.py",
            "ChatGPT": "maximum_total_beauty_of_the_gardens_chatgpt.py",
            "Gemini": "maximum_total_beauty_of_the_gardens_gemini.py",
            "Claude": "maximum_total_beauty_of_the_gardens_claude.py" 
        },
        {
           "problem_name": "minimum_cost_to_make_array_equal",
            "generated_solutions": "minimum_cost_to_make_array_equal.py",
            "ChatGPT": "minimum_cost_to_make_array_equal_chatgpt.py",
            "Gemini": "minimum_cost_to_make_array_equal_gemini.py",
            "Claude": "minimum_cost_to_make_array_equal_claude.py" 
        },
        {
           "problem_name": "maximum_total_beauty_of_the_gardens",
            "generated_solutions": "maximum_total_beauty_of_the_gardens.py",
            "ChatGPT": "maximum_total_beauty_of_the_gardens_chatgpt.py",
            "Gemini": "maximum_total_beauty_of_the_gardens_gemini.py",
            "Claude": "maximum_total_beauty_of_the_gardens_claude.py" 
        },
        {
            "problem_name": "maximum_strength_of_a_group",
            "generated_solutions": "maximum_strength_of_a_group.py",
            "ChatGPT": "maximum_strength_of_a_group_chatgpt.py",
            "Gemini": "maximum_strength_of_a_group_gemini.py",
            "Claude": "maximum_strength_of_a_group_claude.py"
        }
        # You can add more tasks here...
    ]

    # Define the folder names in the desired order.
    folders = ["generated_solutions", "ChatGPT", "Gemini", "Claude"]

    # Aggregated statistics per folder (across tasks) for the bar chart.
    aggregate_stats = {folder: {"pass": 0, "fail": 0} for folder in folders}

    # Results per task for the HTML summary table.
    # Structure: { problem_name: { folder: {"pass": 0/1, "fail": 0/1}, ... } }
    task_results = {}

    # Create a list of futures to run all tasks concurrently.
    futures = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for task in tasks:
            problem_name = task["problem_name"]
            task_results[problem_name] = {}
            for folder in folders:
                # Get the file name for the current folder.
                file_name = task.get(folder)
                if not file_name:
                    # Skip if the task does not have an entry for this folder.
                    continue
                filepath = os.path.join(folder, file_name)
                future = executor.submit(run_script, filepath)
                # Append a tuple: (future, problem_name, folder, file_name)
                futures.append((future, problem_name, folder, file_name))

        # Process the results as they are completed.
        for future, problem_name, folder, file_name in futures:
            fp, return_code, stdout, stderr = future.result()
            # Consider a return code of 0 as a pass.
            passed = 1 if return_code == 0 else 0
            failed = 0 if return_code == 0 else 1

            # Save result for the current task and folder.
            task_results[problem_name][folder] = {"pass": passed, "fail": failed}

            # Update aggregate stats.
            aggregate_stats[folder]["pass"] += passed
            aggregate_stats[folder]["fail"] += failed

            print(f"[DEBUG] Problem: {problem_name} | Folder: {folder} | File: {file_name} | Return Code: {return_code}")

    # -----------------------------
    #  Create a grouped bar chart (aggregated stats)
    # -----------------------------
    agg_pass_counts = [aggregate_stats[f]["pass"] for f in folders]
    agg_fail_counts = [aggregate_stats[f]["fail"] for f in folders]

    x = range(len(folders))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 4))
    rects_pass = ax.bar([i - width / 2 for i in x], agg_pass_counts, width, label='Pass', color='green')
    rects_fail = ax.bar([i + width / 2 for i in x], agg_fail_counts, width, label='Fail', color='red')

    ax.set_ylabel('Count')
    ax.set_title('Pass/Fail Comparison Across Folders (Aggregated over Tasks)')
    ax.set_xticks(list(x))
    ax.set_xticklabels(folders)
    ax.legend()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects_pass)
    autolabel(rects_fail)

    plt.tight_layout()
    graph_file = "comparison_graph.png"
    plt.savefig(graph_file)
    plt.close()

    if os.path.exists(graph_file):
        print(f"[INFO] Graph generated and saved as: {graph_file}")
    else:
        print("[ERROR] Graph file was not generated!")

    # ------------------------------------
    #  Build HTML Report with a Multi-Row Table
    # ------------------------------------
    html_file = "comparison_report.html"
    html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Python Solutions Comparison Report</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 20px;
    }}
    table {{
      border-collapse: collapse;
      width: 90%;
      margin-top: 20px;
    }}
    th, td {{
      border: 1px solid #ccc;
      padding: 8px;
      text-align: center;
    }}
    th {{
      background-color: #f2f2f2;
    }}
  </style>
</head>
<body>
  <h1>Python Solutions Comparison Report</h1>
  <!--
      Comparing multiple Python solutions (tasks) across four folders:
          generated_solutions, ChatGPT, Gemini, and Claude.
  -->
  <h2>Pass/Fail Bar Chart (Aggregated over Tasks)</h2>
  <img src="{graph_file}" alt="Pass/Fail Comparison Graph" style="max-width: 600px;">

  <h2>Summary Table</h2>
  <table>
    <thead>
      <tr>
        <th rowspan="2">File</th>
        <th colspan="2">generated_solutions</th>
        <th colspan="2">ChatGPT</th>
        <th colspan="2">Gemini</th>
        <th colspan="2">Claude</th>
      </tr>
      <tr>
        <th>Pass</th>
        <th>Fail</th>
        <th>Pass</th>
        <th>Fail</th>
        <th>Pass</th>
        <th>Fail</th>
        <th>Pass</th>
        <th>Fail</th>
      </tr>
    </thead>
    <tbody>
"""

    # For each task, prepare a table row.
    for task in tasks:
        problem_name = task["problem_name"]
        html_content += f"      <tr>\n"
        html_content += f"        <td>{problem_name}</td>\n"
        for folder in folders:
            # Retrieve result for this task and folder; if missing, assume N/A.
            result = task_results.get(problem_name, {}).get(folder, {"pass": "N/A", "fail": "N/A"})
            html_content += f"        <td>{result['pass']}</td>\n"
            html_content += f"        <td>{result['fail']}</td>\n"
        html_content += "      </tr>\n"

    html_content += """    </tbody>
  </table>
</body>
</html>
"""

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"[INFO] Comparison report generated: {html_file}")


if __name__ == "__main__":
    main()

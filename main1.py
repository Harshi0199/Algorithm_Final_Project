import json
import re
import os


def slugify(text: str) -> str:
    """
    Convert a given text into a slug suitable for file naming.

    This function:
      - Converts the text to lowercase.
      - Replaces any sequence of non-alphanumeric characters with a single underscore.
      - Strips leading or trailing underscores.

    Args:
        text (str): Original text (for example, the task name).

    Returns:
        str: A slug suitable for a file name.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_')


def prefix_lines(text: str, prefix: str = "# ") -> str:
    """
    Prefix every non-empty line of the provided text with the given prefix.

    Args:
        text (str): Multi-line text.
        prefix (str): The prefix string to add at the start of each non-empty line.

    Returns:
        str: The resulting text with each line prefixed.
    """
    lines = text.strip().splitlines()
    return "\n".join(prefix + line for line in lines if line.strip())


def create_individual_solution_files(json_filename: str, output_folder: str):
    """
    Reads a JSON file (dp_sampled_10_each.json) that contains Python problems and creates an individual
    Python file for each problem. Each file will include:
      - Header comments with the problem index, task name, difficulty, and description.
      - The test case generator code.
      - The test cases.

    The canonical solution is removed as the test_case_generator already contains the solution code.

    Files are saved using the task name (converted to a slug) as the file name, placed in the specified folder.

    Args:
        json_filename (str): The JSON file containing the problems.
        output_folder (str): The folder to store the generated Python files.
    """
    # Create the output folder if it does not exist.
    os.makedirs(output_folder, exist_ok=True)

    with open(json_filename, "r", encoding="utf-8") as file:
        problems = json.load(file)

    for idx, problem in enumerate(problems):
        # Retrieve details from the JSON.
        problem_idx = problem.get("problem_idx", idx)
        task_name = problem.get("task_name", "Unnamed Problem")
        difficulty = problem.get("difficulty", "Unknown")
        description = problem.get("description", "No Description Provided")
        test_case_generator = problem.get("test_case_generator", "").strip()
        test_cases = problem.get("test_case", "").strip()

        # Generate a valid file name based on the task name.
        slug = slugify(task_name)
        filename = os.path.join(output_folder, f"{slug}.py")

        # Prepare the description text as comments.
        description_comment = prefix_lines(description)

        # Build the file content.
        file_content = f'''# Problem {problem_idx}: {task_name}
# Difficulty: {difficulty}
# Description:
{description_comment}

# --------------------------------------
# Test Case Generator Code:
{test_case_generator}

# --------------------------------------
# Test Cases:
{test_cases}

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
'''
        # Write the content into the file.
        with open(filename, "w", encoding="utf-8") as out_file:
            out_file.write(file_content)

        print(f"Created file: {filename}")


if __name__ == '__main__':
    json_filename = "dp_sampled_hard.json"  # JSON file in the current project
    output_folder = "different_generated_solutions"  # Folder to store the Python files
    create_individual_solution_files(json_filename, output_folder)

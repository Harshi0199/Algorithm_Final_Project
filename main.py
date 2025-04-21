import json
import random
from collections import defaultdict


def extract_dynamic_programming_problems(input_file: str) -> list:
    """
    Reads the JSON dataset from the given file and filters problems that use
    dynamic programming as one of their algorithms.

    Args:
        input_file (str): Path to the JSON file.

    Returns:
        list: A list of problem objects whose 'algorithms' list contains 'dynamic_programming'.
    """
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)

    dp_problems = [
        item for item in data if 'greedy' in item.get('algorithms', [])
    ]
    return dp_problems


def group_by_difficulty(problems: list) -> dict:
    """
    Groups the given list of problems by their difficulty level.

    Args:
        problems (list): List of problem objects.

    Returns:
        dict: A dictionary with keys as difficulty levels ('Easy', 'Medium', 'Hard')
              and values as lists of problems.
    """
    groups = defaultdict(list)
    for problem in problems:
        difficulty = problem.get("difficulty", "Hard")
        groups[difficulty].append(problem)
    return groups


def sample_problems(groups: dict, sample_size: int) -> list:
    """
    Samples sample_size problems from each difficulty group.

    Args:
        groups (dict): Dictionary with difficulties as keys and list of problems as values.
        sample_size (int): Number of problems to select from each difficulty level.

    Returns:
        list: A combined list of sampled problems.

    Raises:
        ValueError: If the number of problems available for any difficulty is less than sample_size.
    """
    sampled = []
    for diff in ['Hard']:
        problems = groups.get(diff, [])
        if len(problems) < sample_size:
            raise ValueError(
                f"Not enough problems for difficulty '{diff}': "
                f"found {len(problems)}, needed {sample_size}."
            )
        sampled.extend(random.sample(problems, sample_size))
    return sampled


def save_problems(problems: list, output_file: str) -> None:
    """
    Saves the list of problem objects to the output JSON file with indentation.

    Args:
        problems (list): The list of problem objects.
        output_file (str): Path to save the JSON file.
    """
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(problems, outfile, indent=4)
    print(f"Saved {len(problems)} problems to {output_file}")


if __name__ == '__main__':
    # File that contains the full dataset.
    input_filename = 'dataset_with_difficulty_and_algorithm.json'
    # New JSON file where 10 easy, 10 medium, and 10 hard dynamic programming problems will be saved.
    output_filename = 'dp_sampled_hard.json'
    sample_size = 3

    # Extract dynamic programming problems
    dp_problems = extract_dynamic_programming_problems(input_filename)
    print(f"Found {len(dp_problems)} dynamic programming problems.")

    # Group the problems by difficulty
    groups = group_by_difficulty(dp_problems)
    print("Counts by difficulty in the dynamic programming subset:")
    for diff in ['Hard']:
        print(f"{diff}: {len(groups.get(diff, []))}")

    try:
        # Sample 10 problems from each difficulty
        sampled_problems = sample_problems(groups, sample_size)
    except ValueError as err:
        print(err)
        exit(1)

    # Save the sampled problems into a new file.
    save_problems(sampled_problems, output_filename)

    # Print the counts of problems in the new file
    final_counts = {'Hard': 0}
    for problem in sampled_problems:
        diff = problem.get("difficulty", "Hard")
        if diff in final_counts:
            final_counts[diff] += 1

    print("\nSampled problem counts by difficulty:")
    print(f"Hard: {final_counts['Hard']}")

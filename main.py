import sys
import os
from utils import get_puzzle_input


def main(day):
    input_data = get_puzzle_input(day)

    day_folder = f"day{day:02d}"
    input_folder = os.path.join(day_folder, "input")
    solutions_folder = os.path.join(day_folder, "solutions")
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(solutions_folder, exist_ok=True)

    input_file_path = os.path.join(
        input_folder,
        "input.txt",
    )
    with open(input_file_path, "w") as input_file:
        input_file.write(input_data)

    part1_file_path = os.path.join(
        solutions_folder,
        "solution_part1.py",
    )
    part2_file_path = os.path.join(
        solutions_folder,
        "solution_part2.py",
    )
    test_part1_file_path = os.path.join(
        solutions_folder,
        "test_solution_part1.py",
    )
    test_part2_file_path = os.path.join(
        solutions_folder,
        "test_solution_part2.py",
    )

    if not os.path.exists(part1_file_path):
        with open(part1_file_path, "w") as part1_file:
            part1_file.write("# Solution for Part 1\n")
    if not os.path.exists(part2_file_path):
        with open(part2_file_path, "w") as part2_file:
            part2_file.write("# Solution for Part 2\n")
    if not os.path.exists(test_part1_file_path):
        with open(test_part1_file_path, "w") as test_part1_file:
            test_part1_file.write("# Tests for Part 1\n")
    if not os.path.exists(test_part2_file_path):
        with open(test_part2_file_path, "w") as test_part2_file:
            test_part2_file.write("# Tests for Part 2\n")

    print(f"Day {day} input saved to {input_file_path}")
    print(f"Solution and test files created at {solutions_folder}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <day>")
        sys.exit(1)
    day = int(sys.argv[1])
    main(day)

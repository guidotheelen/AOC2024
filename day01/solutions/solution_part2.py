# Solution for Part 2

from solution_part1 import parse_input


def simScore(number, list):
    return sum(
        [1 for i in list if i == number],
    )


file_path = "/Users/guidotheelen/Projects/AOC2024/day01/inputs/input_part1.txt"
first_column, second_column = parse_input(file_path)

answer = sum([simScore(i, second_column) * i for i in first_column])

print(f"Answer part 2: {answer}")

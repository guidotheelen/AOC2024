# Solution for Part 1


import re


def get_string(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()


def get_multiply_functions(input):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern, input)


def evaluate_multiplications(multiply_functions):
    results = []
    for func in multiply_functions:
        numbers = list(map(int, re.findall(r"\d+", func)))
        results.append(numbers[0] * numbers[1])
    return results


input = get_string(
    "/Users/guidotheelen/Projects/AOC2024/day03/input/input.txt",
)
multiply_functions = get_multiply_functions(input)
results = evaluate_multiplications(multiply_functions)

print(f"Answer part 1: {sum(results)}")

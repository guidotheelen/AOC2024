# Solution for Part 2

import re

from solution_part1 import get_string


def process_instructions(input):
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    instructions = re.findall(pattern, input)

    enabled = True
    result = 0

    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif enabled and instruction.startswith("mul"):
            x, y = map(int, re.findall(r"\d+", instruction))
            result += x * y

    return result


input = get_string(
    "/Users/guidotheelen/Projects/AOC2024/day03/input/input.txt",
)
results = process_instructions(input)

print(f"Answer part 2: {results}")

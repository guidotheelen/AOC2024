# Solution for Part 1

import re


def get_lines(file_path):
    with open(file_path, "r") as file:
        return [line.rstrip("\n") for line in file]


def get_matches_in_line(line, pattern):
    return len(pattern.findall(line))


def get_vertical_lines(lines):
    return ["".join(line) for line in zip(*lines)]


def get_diagonal_lines(lines):
    m = len(lines)
    n = max(len(line) for line in lines)
    diagonals = []

    # Diagonals from top-left to bottom-right (i + j = k)
    for k in range(m + n - 1):
        diag = ""
        for i in range(m):
            j = k - i
            if 0 <= j < len(lines[i]):
                diag += lines[i][j]
        if diag:
            diagonals.append(diag)

    # Diagonals from top-right to bottom-left (j - i = k)
    for k in range(n - 1, -m, -1):
        diag = ""
        for i in range(m):
            j = i + k
            if 0 <= j < len(lines[i]):
                diag += lines[i][j]
        if diag:
            diagonals.append(diag)

    return diagonals


lines = get_lines("/Users/guidotheelen/Projects/AOC2024/day04/input/input.txt")
vertical_lines = get_vertical_lines(lines)
diagonal_lines = get_diagonal_lines(lines)
all_lines = lines + vertical_lines + diagonal_lines

XMAS_REGEX = r"(?=(XMAS|SAMX))"
pattern = re.compile(XMAS_REGEX)
total_matches = sum([get_matches_in_line(line, pattern) for line in all_lines])

print(f"Answer part 1: {total_matches}")

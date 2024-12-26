# Solution for Part 1

from itertools import product


def get_lines(file_path):
    with open(file_path, "r") as file:
        return [line.rstrip("\n") for line in file]


def solve():
    lines = get_lines(
        "/Users/guidotheelen/Projects/AOC2024/day07/input/input.txt",
    )
    total = 0

    for line in lines:
        left_part, right_part = line.split(":")
        target = int(left_part.strip())
        numbers = list(map(int, right_part.split()))

        # If there's only 1 number, that must directly match the target
        if len(numbers) == 1:
            if numbers[0] == target:
                total += target
            continue

        # Let's see if any +/* combination yields 'target'.
        # We'll do a DFS or iterative approach over all 2^(n-1) combos.
        n = len(numbers)
        possible = False

        # We can represent each combination by a bitmask from 0..(2^(n-1) -1).
        # Where bit i determines whether the i-th operator is + (0) or * (1).

        for ops in product(["+", "*"], repeat=(n - 1)):
            # Evaluate left-to-right
            value = numbers[0]
            for i, op in enumerate(ops, start=1):
                if op == "+":
                    value = value + numbers[i]
                else:  # op == '*'
                    value = value * numbers[i]

            if value == target:
                possible = True
                break

        if possible:
            total += target

    print(total)


if __name__ == "__main__":
    solve()

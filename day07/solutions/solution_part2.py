# Solution for Part 2

from itertools import product

from solution_part1 import get_lines


def solve():
    lines = get_lines(
        "/Users/guidotheelen/Projects/AOC2024/day07/input/input.txt",
    )
    total = 0

    for line in lines:
        line = line.strip()
        left, right = line.split(":")
        target = int(left.strip())
        numbers = list(map(int, right.split()))

        # If only one number, it must match exactly
        if len(numbers) == 1:
            if numbers[0] == target:
                total += target
            continue

        # We'll try all combinations of operators in the (n-1) slots
        n = len(numbers)
        possible = False

        # Each operator slot can be '+', '*', or '||'
        for ops in product(["+", "*", "||"], repeat=(n - 1)):
            value = numbers[0]
            # Evaluate left-to-right with the chosen operators
            for i, op in enumerate(ops, start=1):
                next_num = numbers[i]
                if op == "+":
                    value = value + next_num
                elif op == "*":
                    value = value * next_num
                else:  # op == '||'
                    # Concatenate as strings
                    value_str = str(value) + str(next_num)
                    value = int(value_str)

            if value == target:
                possible = True
                break

        if possible:
            total += target

    print(total)


if __name__ == "__main__":
    solve()

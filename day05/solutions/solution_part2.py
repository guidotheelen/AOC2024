# Solution for Part 2

from solution_part1 import (
    filter_updates,
    middel_number_from_list,
    parse_input,
)
from collections import defaultdict


def fix_update(rules, update):
    filtered_rules = defaultdict(set)
    for i in update:
        filtered_rules[i] = set(b for a, b in rules if a == i) & set(update)

    ordered_keys = sorted(
        filtered_rules, key=lambda k: len(filtered_rules[k]), reverse=True
    )
    return ordered_keys


input_file = "/Users/guidotheelen/Projects/AOC2024/day05/input/input.txt"
order_rules, updates = parse_input(input_file)
invalid_updates = filter_updates(updates, order_rules, valid=False)
ordered_invalid_updates = [
    fix_update(order_rules, update) for update in invalid_updates
]
sum_middle_numbers = sum(
    middel_number_from_list(update) for update in ordered_invalid_updates
)

print("Solution part 2:", sum_middle_numbers)

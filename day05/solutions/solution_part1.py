# Solution for Part 1


def parse_input(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()

    order_rules = []
    updates = []
    is_update_section = False

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if "," in line:
            is_update_section = True

        if is_update_section:
            updates.append(list(map(int, line.split(","))))
        else:
            order_rules.append(tuple(map(int, line.split("|"))))

    return order_rules, updates


def is_valid_update(update, order_rules):
    for rule in order_rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True


def filter_updates(updates, order_rules, valid=True):
    return [
        update
        for update in updates
        if is_valid_update(
            update,
            order_rules,
        )
        == valid
    ]


def middel_number_from_list(numbers):
    return numbers[len(numbers) // 2]


input_file = "/Users/guidotheelen/Projects/AOC2024/day05/input/input.txt"
order_rules, updates = parse_input(input_file)
valid_updates = filter_updates(updates, order_rules)
sum_middle_numbers = sum(middel_number_from_list(update) for update in valid_updates)

print("Solution part 1:", sum_middle_numbers)

# Solution for Part 1


def parse_input(file_path):
    first_column = []
    second_column = []
    with open(file_path, "r") as file:
        for line in file:
            values = line.split()
            first_column.append(int(values[0]))
            second_column.append(int(values[1]))
    return first_column, second_column


def distList(list1, list2):
    if len(list1) != len(list2):
        raise IndexError("Lists must have the same length")

    return [abs(list1[i] - list2[i]) for i in range(len(list1))]


file_path = "/Users/guidotheelen/Projects/AOC2024/day01/inputs/input_part1.txt"
first_column, second_column = parse_input(file_path)

first_column.sort()
second_column.sort()

answer = sum(distList(first_column, second_column))

print(f"Answer part 1: {answer}")

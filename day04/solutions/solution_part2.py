# Solution for Part 2

from solution_part1 import get_lines


def get_3_by_3_squares(lines):
    squares = []
    num_rows = len(lines)
    num_cols = len(lines[0]) if lines else 0
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            square = "".join(lines[i + k][j : j + 3] for k in range(3))
            squares.append(square)
    return squares


def dot_every_even_chars(square):
    return "".join(char if i % 2 == 0 else "." for i, char in enumerate(square))


def filter_squares(squares, condition):
    return [square for square in squares if condition(square)]


def middle_is_A(square):
    return square[4] == "A"


def one_A(square):
    return square.count("A") == 1


def no_X(square):
    return "X" not in square


def two_M(square):
    return square.count("M") == 2


def two_S(square):
    return square.count("S") == 2


def length_is_9(square):
    return len(square) == 9


def no_double_in_middle(square):
    return "S.A.S" not in square and "M.A.M" not in square


lines = get_lines("/Users/guidotheelen/Projects/AOC2024/day04/input/input.txt")
squares = get_3_by_3_squares(lines)
dotted_squares = [dot_every_even_chars(square) for square in squares]

filters = [
    middle_is_A,
    one_A,
    no_X,
    two_M,
    two_S,
    length_is_9,
    no_double_in_middle,
]
cleaned_squares = dotted_squares
for condition in filters:
    cleaned_squares = filter_squares(cleaned_squares, condition)

answer = len(cleaned_squares)
print(f"Answer part 2: {answer}")

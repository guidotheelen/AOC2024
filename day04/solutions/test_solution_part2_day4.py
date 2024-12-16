# Tests for Part 2


import unittest
from solution_part2 import (
    get_top_left_diagonals,
    get_top_right_diagonals,
)


class TestSolutionPart2(unittest.TestCase):
    def test_xmas(self):
        lines = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX",
        ]

        top_left_diagonals = get_top_left_diagonals(lines)
        top_right_diagonals = get_top_right_diagonals(lines)

        print(top_left_diagonals)
        print(top_right_diagonals)

        self.assertEqual(1, 9)


if __name__ == "__main__":
    unittest.main()

# Tests for Part 1
import unittest
import re
from solution_part1 import (
    XMAS_REGEX,
    get_matches_in_line,
    get_vertical_lines,
    get_diagonal_lines,
)


class TestSolutionPart1(unittest.TestCase):
    def test_get_horizontal_matches(self):
        pattern = re.compile(XMAS_REGEX)
        self.assertEqual(get_matches_in_line("XMAS SAMX XMAS", pattern), 3)
        self.assertEqual(get_matches_in_line("XMASXMAS", pattern), 2)
        self.assertEqual(get_matches_in_line("SAMX SAMX", pattern), 2)
        self.assertEqual(get_matches_in_line("NO MATCH", pattern), 0)

    def test_get_vertical_lines(self):
        lines = ["ABC", "DEF", "GHI"]
        expected = ["ADG", "BEH", "CFI"]
        self.assertEqual(get_vertical_lines(lines), expected)

        lines = ["A", "B", "C"]
        expected = ["ABC"]
        self.assertEqual(get_vertical_lines(lines), expected)

        lines = ["AB", "CD"]
        expected = ["AC", "BD"]
        self.assertEqual(get_vertical_lines(lines), expected)

    def test_get_diagonal_lines(self):
        lines = ["ABC", "DEF", "GHI"]
        expected = ["A", "BD", "CEG", "FH", "I", "C", "BF", "AEI", "DH", "G"]
        self.assertEqual(get_diagonal_lines(lines), expected)

        lines = ["AB", "CD"]
        expected = ["A", "BC", "D", "B", "AD", "C"]
        self.assertEqual(get_diagonal_lines(lines), expected)

    def test_all_lines(self):
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
        vertical_lines = get_vertical_lines(lines)
        diagonal_lines = get_diagonal_lines(lines)
        all_lines = lines + vertical_lines + diagonal_lines

        pattern = re.compile(XMAS_REGEX)
        total_matches = sum(
            [get_matches_in_line(line, pattern) for line in all_lines],
        )
        self.assertEqual(total_matches, 18)


if __name__ == "__main__":
    unittest.main()

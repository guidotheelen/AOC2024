import unittest
from day02.solutions.solution_part1 import (
    vary_check,
    report_is_only_decreasing,
)
from solution_part1 import distList, parse_input
import tempfile
import os

# Tests for Part 1


class TestParseInput(unittest.TestCase):

    def test_parse_input_with_valid_data(self):
        test_data = "1   2\n3   4\n5   6\n"
        expected_first_column = [1, 3, 5]
        expected_second_column = [2, 4, 6]

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(test_data.encode())
            temp_file_path = temp_file.name

        first_column, second_column = parse_input(temp_file_path)
        os.remove(temp_file_path)

        self.assertEqual(first_column, expected_first_column)
        self.assertEqual(second_column, expected_second_column)

    def test_parse_input_with_empty_file(self):
        test_data = ""
        expected_first_column = []
        expected_second_column = []

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(test_data.encode())
            temp_file_path = temp_file.name

        first_column, second_column = parse_input(temp_file_path)
        os.remove(temp_file_path)

        self.assertEqual(first_column, expected_first_column)
        self.assertEqual(second_column, expected_second_column)

    def test_parse_input_with_invalid_data(self):
        test_data = "1   a\n3   4\n5   6\n"

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(test_data.encode())
            temp_file_path = temp_file.name

        with self.assertRaises(ValueError):
            parse_input(temp_file_path)

        os.remove(temp_file_path)


class TestDistList(unittest.TestCase):

    def test_distList_with_positive_numbers(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        expected_result = [3, 3, 3]
        self.assertEqual(distList(list1, list2), expected_result)

    def test_distList_with_negative_numbers(self):
        list1 = [-1, -2, -3]
        list2 = [-4, -5, -6]
        expected_result = [3, 3, 3]
        self.assertEqual(distList(list1, list2), expected_result)

    def test_distList_with_mixed_numbers(self):
        list1 = [1, -2, 3]
        list2 = [-4, 5, -6]
        expected_result = [5, 7, 9]
        self.assertEqual(distList(list1, list2), expected_result)

    def test_distList_with_zeros(self):
        list1 = [0, 0, 0]
        list2 = [0, 0, 0]
        expected_result = [0, 0, 0]
        self.assertEqual(distList(list1, list2), expected_result)

    def test_distList_with_different_lengths(self):
        list1 = [1, 2]
        list2 = [3, 4, 5]
        with self.assertRaises(IndexError):
            distList(list1, list2)


class TestReportIsOnlyDecreasing(unittest.TestCase):

    def test_report_is_only_decreasing_with_decreasing_values(self):
        report = [4, 3, 2, 1]
        self.assertTrue(report_is_only_decreasing(report))

    def test_report_is_only_decreasing_with_increasing_values(self):
        report = [1, 2, 3, 4]
        self.assertFalse(report_is_only_decreasing(report))

    def test_report_is_only_decreasing_with_equal_values(self):
        report = [1, 1, 1, 1]
        self.assertFalse(report_is_only_decreasing(report))

    def test_report_is_only_decreasing_with_mixed_values(self):
        report = [4, 3, 4, 3]
        self.assertFalse(report_is_only_decreasing(report))

    def test_report_is_only_decreasing_with_single_value(self):
        report = [1]
        self.assertTrue(report_is_only_decreasing(report))

    def test_report_is_only_decreasing_with_two_values_decreasing(self):
        report = [2, 1]
        self.assertTrue(report_is_only_decreasing(report))

    def test_report_is_only_decreasing_with_two_values_increasing(self):
        report = [1, 2]
        self.assertFalse(report_is_only_decreasing(report))


class TestVaryCheck(unittest.TestCase):

    def test_vary_check_with_valid_data(self):
        report = [1, 2, 3, 4]
        self.assertTrue(vary_check(report))

    def test_vary_check_with_invalid_data(self):
        report = [1, 5, 3, 4]
        self.assertFalse(vary_check(report))

    def test_vary_check_with_exact_difference(self):
        report = [1, 4, 7, 10]
        self.assertTrue(vary_check(report))

    def test_vary_check_with_negative_values(self):
        report = [-1, -2, -3, -4]
        self.assertTrue(vary_check(report))

    def test_vary_check_with_mixed_values(self):
        report = [1, -1, 2, -2]
        self.assertFalse(vary_check(report))

    def test_vary_check_with_single_value(self):
        report = [1]
        self.assertTrue(vary_check(report))

    def test_vary_check_with_two_values_within_limit(self):
        report = [1, 3]
        self.assertTrue(vary_check(report))

    def test_vary_check_with_two_values_exceeding_limit(self):
        report = [1, 5]
        self.assertFalse(vary_check(report))


if __name__ == "__main__":
    unittest.main()

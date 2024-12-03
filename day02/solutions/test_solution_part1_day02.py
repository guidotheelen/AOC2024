# Tests for Part 1

import os
import tempfile
import unittest

from day02.solutions.solution_part1 import (
    get_reports,
)


class TestGetReports(unittest.TestCase):

    def test_get_reports_with_valid_data(self):
        test_data = "1 2\n3 4\n5 6\n"
        expected_result = [[1, 2], [3, 4], [5, 6]]

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(test_data.encode())
            temp_file_path = temp_file.name

        result = get_reports(temp_file_path)
        os.remove(temp_file_path)

        self.assertEqual(result, expected_result)

    def test_get_reports_with_empty_file(self):
        test_data = ""
        expected_result = []

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(test_data.encode())
            temp_file_path = temp_file.name

        result = get_reports(temp_file_path)
        os.remove(temp_file_path)

        self.assertEqual(result, expected_result)

    def test_get_reports_with_invalid_data(self):
        test_data = "1 a\n3 4\n5 6\n"

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(test_data.encode())
            temp_file_path = temp_file.name

        with self.assertRaises(ValueError):
            get_reports(temp_file_path)

        os.remove(temp_file_path)


if __name__ == "__main__":
    unittest.main()

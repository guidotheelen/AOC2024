# Solution for Part 2

from solution_part1 import (
    get_reports,
    report_is_only_decreasing,
    report_is_only_increasing,
    vary_check,
)


def alternative_arrays(report):
    # Create a list of all possible arrays with one element removed
    return [report[:i] + report[i + 1 :] for i in range(len(report))]


def is_valid_array(report):
    return (
        report_is_only_increasing(report) or report_is_only_decreasing(report)
    ) and vary_check(report)


reports = get_reports(
    "/Users/guidotheelen/Projects/AOC2024/day02/input/input.txt",
)

valid_reports = [report for report in reports if is_valid_array(report)]

invalid_reports = [reports for reports in reports if reports not in valid_reports]

still_valid_reports = [
    report
    for report in invalid_reports
    if any(is_valid_array(array) for array in alternative_arrays(report))
]

print(f"Answer part 2: {len(still_valid_reports) + len(valid_reports)}")

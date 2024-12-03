# Solution for Part 1


def get_reports(file_path):
    with open(file_path, "r") as file:
        return [list(map(int, line.split())) for line in file]


def report_is_only_increasing(report):
    return all(
        earlier < later
        for earlier, later in zip(
            report,
            report[1:],
        )
    )


def report_is_only_decreasing(report):
    return all(
        earlier > later
        for earlier, later in zip(
            report,
            report[1:],
        )
    )


def vary_check(report):
    return all(
        abs(later - earlier) <= 3
        for earlier, later in zip(
            report,
            report[1:],
        )
    )


reports = get_reports(
    "/Users/guidotheelen/Projects/AOC2024/day02/input/input.txt",
)
valid_reports = [
    report
    for report in reports
    if (report_is_only_increasing(report) or report_is_only_decreasing(report))
    and vary_check(report)
]

print(f"Answer part 1: {len(valid_reports)}")

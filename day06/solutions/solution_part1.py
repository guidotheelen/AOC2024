def get_lines(file_path):
    with open(file_path, "r") as file:
        return [line.rstrip("\n") for line in file]


def solve():
    lines = get_lines(
        "/Users/guidotheelen/Projects/AOC2024/day06/input/input.txt",
    )
    height = len(lines)
    width = len(lines[0])

    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    guard_row, guard_col = None, None
    direction_idx = None

    direction_map = {
        "^": 0,  # up
        ">": 1,  # right
        "v": 2,  # down
        "<": 3,  # left
    }

    for r in range(height):
        for c in range(width):
            char = lines[r][c]
            if char in direction_map:
                guard_row, guard_col = r, c
                direction_idx = direction_map[char]
                break
        if guard_row is not None:
            break

    if guard_row is None or direction_idx is None:
        print("No guard found")
        return

    visited = set()
    visited.add((guard_row, guard_col))

    while True:
        dr, dc = DIRECTIONS[direction_idx]

        nr, nc = guard_row + dr, guard_col + dc

        out_of_bounds = nr < 0 or nr >= height or nc < 0 or nc >= width

        if out_of_bounds:
            break

        if lines[nr][nc] == "#":
            direction_idx = (direction_idx + 1) % len(DIRECTIONS)
        else:
            guard_row, guard_col = nr, nc
            visited.add((guard_row, guard_col))

    print(f"Solution part 1: ${len(visited)}")


if __name__ == "__main__":
    solve()

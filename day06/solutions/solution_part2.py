# Solution for Part 2

from solution_part1 import get_lines


def solve():
    lines = get_lines(
        "/Users/guidotheelen/Projects/AOC2024/day06/input/input.txt",
    )
    height = len(lines)
    width = len(lines[0])

    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    dir_map = {
        "^": 0,  # up
        ">": 1,  # right
        "v": 2,  # down
        "<": 3,  # left
    }

    guard_start_r = None
    guard_start_c = None
    guard_start_dir = None

    for r in range(height):
        for c in range(width):
            ch = lines[r][c]
            if ch in dir_map:
                guard_start_r = r
                guard_start_c = c
                guard_start_dir = dir_map[ch]
                break
        if guard_start_r is not None:
            break

    if guard_start_r is None:
        print("No guard found")
        return

    grid = [list(row) for row in lines]

    def simulate_with_extra_obstacle(r_obst, c_obst):
        grid[r_obst][c_obst] = "#"

        row, col = guard_start_r, guard_start_c
        dir_idx = guard_start_dir

        visited_states = set()

        while True:
            state = (row, col, dir_idx)
            if state in visited_states:
                grid[r_obst][c_obst] = "."
                return False
            visited_states.add(state)

            dr, dc = DIRECTIONS[dir_idx]
            nr, nc = row + dr, col + dc

            if not (0 <= nr < height and 0 <= nc < width):
                grid[r_obst][c_obst] = "."  # Remove obstacle
                return True

            if grid[nr][nc] == "#":
                dir_idx = (dir_idx + 1) % 4
            else:
                # Move forward
                row, col = nr, nc

    loop_positions = 0

    for r in range(height):
        for c in range(width):
            if grid[r][c] == "#":
                continue
            if r == guard_start_r and c == guard_start_c:
                continue

            left_map = simulate_with_extra_obstacle(r, c)
            if not left_map:
                # If the guard did NOT leave (i.e., got stuck in loop),
                # then this is a valid position for an obstruction.
                loop_positions += 1

    print(f"Solution part 2: ${loop_positions}")


if __name__ == "__main__":
    solve()

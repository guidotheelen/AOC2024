# Solution for Part 1


def get_puzzle_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()


def parse_disk_map(s):
    disk = []
    is_file = True
    file_id = 0

    for ch in s:
        length = int(ch)
        if length == 0:
            pass
        else:
            if is_file:
                disk.extend([file_id] * length)
                file_id += 1
            else:
                disk.extend(["."] * length)

        is_file = not is_file

    return disk


def find_leftmost_gap_with_file_right(disk):
    for i in range(len(disk) - 1):
        if disk[i] == ".":
            if any(block != "." for block in disk[i + 1 :]):
                return i
    return None


def find_rightmost_block(disk):
    for i in range(len(disk) - 1, -1, -1):
        if disk[i] != ".":
            return i
    return None


def compact_disk(disk):
    while True:
        gap_idx = find_leftmost_gap_with_file_right(disk)
        if gap_idx is None:
            break

        block_idx = find_rightmost_block(disk)
        if block_idx is None:
            break

        disk[gap_idx] = disk[block_idx]
        disk[block_idx] = "."

    return disk


def compute_checksum(disk):
    total = 0
    for pos, block in enumerate(disk):
        if block != ".":
            total += pos * block
    return total


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(
        "/Users/guidotheelen/Projects/AOC2024/day09/input/input.txt"
    )
    disk_puzzle = parse_disk_map(puzzle_input)
    compact_disk(disk_puzzle)
    result_checksum = compute_checksum(disk_puzzle)

    print("Solution part 1:", result_checksum)

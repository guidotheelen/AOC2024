from solution_part1 import parse_disk_map, compute_checksum, get_puzzle_input


def compact_disk_wholefiles(disk):
    file_ids = sorted({blk for blk in disk if blk != "."}, reverse=True)

    for fid in file_ids:
        file_indices = [i for i, b in enumerate(disk) if b == fid]
        if not file_indices:
            continue

        file_size = len(file_indices)
        leftmost_index = min(file_indices)

        candidate_start = None
        current_run_length = 0

        free_spans = []

        for i in range(leftmost_index):
            if disk[i] == ".":
                if candidate_start is None:
                    candidate_start = i
                current_run_length += 1
            else:
                if candidate_start is not None:
                    free_spans.append((candidate_start, current_run_length))
                candidate_start = None
                current_run_length = 0

        if candidate_start is not None:
            free_spans.append((candidate_start, current_run_length))

        move_start = None
        for start, length in free_spans:
            if length >= file_size:
                move_start = start
                break

        if move_start is not None:
            for idx in file_indices:
                disk[idx] = "."
            for offset in range(file_size):
                disk[move_start + offset] = fid

    return disk


if __name__ == "__main__":
    puzzle_input = puzzle_input = get_puzzle_input(
        "/Users/guidotheelen/Projects/AOC2024/day09/input/input.txt",
    )

    disk = parse_disk_map(puzzle_input)

    compact_disk_wholefiles(disk)

    cheksum = compute_checksum(disk)
    print("Solution part 2:", cheksum)

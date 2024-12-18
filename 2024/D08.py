from collections import Counter
from itertools import combinations, count


def find_antinodes_all_distances(x1, y1, x2, y2, n_rows, n_cols):

    possible_antinodes = []

    for D in count(1):
        out_of_range_count = 0

        for (start_x, start_y, end_x, end_y) in [(x1, y1, x2, y2), (x2, y2, x1, y1)]:
            row = start_x + D * (end_x - start_x)
            col = start_y + D * (end_y - start_y)

            if 0 <= row < n_rows and 0 <= col < n_cols:
                possible_antinodes.append((row, col))
            else:
                out_of_range_count += 1

        if out_of_range_count == 2:
            break

    return possible_antinodes


def parse_antenne_locations(grid):

    antenne_locations = {}

    for row_idx, row in enumerate(grid):
        for col_idx, item in enumerate(row):
            if item != ".":
                antenne_locations.setdefault(item, []).append((row_idx, col_idx))

    return antenne_locations


def run(part):

    with open("input.txt", "r") as file:
        grid = [list(line.strip()) for line in file]

    antenne_locations = parse_antenne_locations(grid)

    antinodes = set()

    for antenne in antenne_locations.keys():
        antenne_pairs = list(combinations(antenne_locations[antenne], 2))

        for (x1, y1), (x2, y2) in antenne_pairs:

            if part == "P1":
                possible_antinodes = [ 
                    (x1 + 2 * (x2 - x1), y1 + 2 * (y2 - y1)),
                    (x2 + 2 * (x1 - x2), y2 + 2 * (y1 - y2))
                ]
            elif part == "P2":
                possible_antinodes = find_antinodes_all_distances(x1, y1, x2, y2, len(grid), len(grid[0]))

            for antinode in possible_antinodes:
                antinode_x, antinode_y = antinode
                if (
                    (antinode_x, antinode_y) not in antinodes 
                    and 0 <= antinode_x < len(grid) 
                    and 0 <= antinode_y < len(grid[0]) 
                    and grid[antinode_x][antinode_y] != antenne
                ):
                    antinodes.add((antinode_x, antinode_y))

        if part == "P2":

            all_tuples = [t for pair in antenne_pairs for t in pair]

            counts = Counter(all_tuples)

            for antenne_loc in antenne_locations[antenne]:

                if counts[antenne_loc] > 1 and antenne_loc not in antinodes:
                    antinodes.add(antenne_loc)

    print(len(antinodes))


run("P1")
run("P2")

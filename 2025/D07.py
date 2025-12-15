def parse_input():

    with open("input.txt") as f:
        grid = [list(map(str, line.strip())) for line in f.readlines()]

    start_pos = next(
        (r, c)
        for r, row in enumerate(grid)
        for c, val in enumerate(row)
        if val == "S"
    )

    return grid, start_pos


def get_splits(grid, r, c, visited):

    count = 0

    visited.add((r, c))

    if r + 1 < len(grid) and grid[r+1][c] != '^' and (r+1, c) not in visited:
        count += get_splits(grid, r+1, c, visited)

    if r + 1 < len(grid) and grid[r+1][c] == '^' and (r+1, c) not in visited:
        count += get_splits(grid, r+1, c-1, visited) + get_splits(grid, r+1, c+1, visited) + 1

    return count


def get_paths(grid, r, c, cache={}):

    if (r, c) in cache:
        return cache[(r, c)]

    if r + 1 == len(grid):
        return 1
    
    total_paths = 0

    if r + 1 < len(grid) and grid[r+1][c] != '^':
        total_paths += get_paths(grid, r+1, c, cache)

    if r + 1 < len(grid) and grid[r+1][c] == '^':
        total_paths += get_paths(grid, r+1, c-1, cache) + get_paths(grid, r+1, c+1, cache)

    cache[(r, c)] = total_paths

    return total_paths


grid, start_pos = parse_input()

print(get_splits(grid, start_pos[0], start_pos[1], set()))
print(get_paths(grid, start_pos[0], start_pos[1]))
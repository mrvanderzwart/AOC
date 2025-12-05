import sys
sys.setrecursionlimit(100000)


def parse_input():
    with open('input.txt', 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]

    return grid


def check_adjacent(grid, x, y):

    count = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        count += 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '@'

    return count < 4


def walk(grid, x, y, total, indices=[]):

    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return

    if grid[x][y] == '@' and check_adjacent(grid, x, y):
        total += 1
        indices.append((x, y))

    if x + 1 < len(grid):
        return walk(grid, x + 1, y, total, indices)
    elif y + 1 < len(grid[0]):
        return walk(grid, 0, y + 1, total, indices)

    return total


def P1(grid):

    print(walk(grid, 0, 0, 0))


def P2(grid, total=0):

    while True:
        indices = []
        count = walk(grid, 0, 0, 0, indices)

        if count == 0:
            print(total)
            return

        total += len(indices)

        for x, y in indices:
            grid[x][y] = '.'


grid = parse_input()

P1(grid)
P2(grid)
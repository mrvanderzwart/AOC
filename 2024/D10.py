   
from collections import deque


def find_start_positions(grid):

    return [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 0]


def climb_bfs(grid, start_row, start_column, P1):

    queue = deque([(start_row, start_column)])
    visited = set()
    count = 0
    
    while queue:
        row, column = queue.popleft()
        
        if (
            row < 0 or row >= len(grid) or 
            column < 0 or column >= len(grid[0]) or
            (row, column) in visited and P1
        ):
            continue

        visited.add((row, column))
        
        if grid[row][column] == 9:
            count += 1
            continue
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (
                0 <= row+dx < len(grid) and 0 <= column+dy < len(grid[0]) and
                grid[row+dx][column+dy] == grid[row][column] + 1
            ):
                queue.append((row + dx, column + dy))
    
    return count


def run(grid, start_positions, P1):

    score = 0

    for (row, column) in start_positions:
        score += climb_bfs(grid, row, column, P1)

    print(score)


with open("input.txt", "r") as file:
    grid = [[int(digit) for digit in line.strip()] for line in file]

start_positions = find_start_positions(grid)

run(grid, start_positions, P1=True)
run(grid, start_positions, P1=False)
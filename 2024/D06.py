def find_start_position(grid):

    for i, row in enumerate(grid):
        if "^" in row:
            return i, row.index("^")
        
    return None
    

def patrol_p1(grid, row, column, index, count):

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    dx, dy = directions[index]

    while True:

        if (row+dx) < 0 or (row+dx) >= len(grid) or (column+dy) < 0 or (column+dy) >= len(grid[0]):
            return count

        while grid[row+dx][column+dy] == "#":
            index = (index + 1) % 4
            dx, dy = directions[index]

        if grid[row][column] != "X":
            grid[row][column] = "X"
            count += 1
        
        row, column = row + dx, column + dy


def simulate_loop(grid, row, column, index):

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    dx, dy = directions[index]

    visited = []

    while True:

        if (row+dx) < 0 or (row+dx) >= len(grid) or (column+dy) < 0 or (column+dy) >= len(grid[0]):
            return False
        
        if ((row, column, index) in visited):
            return True

        visited.append((row, column, index))

        while grid[row+dx][column+dy] == "#" or grid[row+dx][column+dy] == "O":
            index = (index + 1) % 4
            dx, dy = directions[index]

        row, column = row + dx, column + dy


def patrol_p2(grid, row, column, index, count):

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    dx, dy = directions[index]

    positions = set()

    while True:

        if (row+dx) < 0 or (row+dx) >= len(grid) or (column+dy) < 0 or (column+dy) >= len(grid[0]):
            return count

        while grid[row+dx][column+dy] == "#":
            index = (index + 1) % 4
            dx, dy = directions[index]

        grid[row][column] = "X"

        row, column = row + dx, column + dy
        
        simulated_grid = [row[:] for row in grid]
        simulated_grid[row][column] = "O"
        
        if (grid[row][column] != "X") and ((row, column) not in positions) and (simulate_loop(simulated_grid, row-dx, column-dy, (index+1)%4)):
            positions.add((row, column))
            count += 1


def P1():

    with open("input.txt", "r") as file:
        grid = [list(line.strip()) for line in file]

    row, column = find_start_position(grid)

    steps = patrol_p1(grid, row, column, 0, 1)

    print(steps)


def P2():

    with open("input.txt", "r") as file:
        grid = [list(line.strip()) for line in file]

    row, column = find_start_position(grid)

    steps = patrol_p2(grid, row, column, 0, 0)

    print(steps)


P1()
P2()

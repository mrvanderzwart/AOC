import copy

from collections import deque


directions = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}


class Robot:

    def __init__(self, x, y):

        self.x = x
        self.y = y


    def step(self, next_x, next_y):

        self.x = next_x
        self.y = next_y


def find_free_spot_horizontally(grid, x, y, instruction):

    dx, dy = directions[instruction]

    positions = []

    while True:

        if grid[x+dx][y+dy] == ".":
            positions.append((x, y))
            grid_after = copy.deepcopy(grid)

            for x, y in positions:
                grid_after[x+dx][y+dy] = grid[x][y]
            grid = grid_after

            return grid
        
        elif grid[x+dx][y+dy] == "#":
            return False
        
        positions.append((x, y))

        x, y = x + dx, y + dy


def find_free_spot_vertically(grid, start, directions):

    grid_after = copy.deepcopy(grid)

    free_spots = []

    stack = deque()

    x, y = start
    dx, dy = directions

    stack.append((x, y))

    positions = []

    visited = set()

    while stack:

        x, y = stack.pop()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        if grid[x][y] == "[":
            stack.append((x, y+1))
        elif grid[x][y] == "]":
            stack.append((x, y-1))

        if grid[x+dx][y+dy] in "[]":
            stack.append((x+dx, y+dy))

        if grid[x+dx][y+dy] == ".":
            free_spots.append((x+dx, y+dy))

        elif grid[x+dx][y+dy] == "#":
            return False

        positions.append((x, y))

    if len(set(row for row, _ in free_spots)):
        for x, y in positions:
            if (x-dx, y-dy) in positions:
                grid_after[x][y] = grid[x-dx][y-dy]
            else:
                grid_after[x][y] = "."
            grid_after[x+dx][y+dy] = grid[x][y]

        grid = grid_after
        return grid


def eval(grid, part):

    gps = 0

    for row_index in range(len(grid)):
        for column_index in range(len(grid[0])):

            if part == "part1" and grid[row_index][column_index] == "O":
                gps += ((100 * row_index) + column_index)
            elif part == "part2" and grid[row_index][column_index] == "[":
                gps += ((100 * row_index) + column_index)\

    return gps


def find_free_spot(grid, x, y, instruction, part):

    dx, dy = directions[instruction]

    if instruction == "<" or instruction == ">" or part == "part1":
        return find_free_spot_horizontally(grid, x+dx, y+dy, instruction)
    else:
        return find_free_spot_vertically(grid, (x+dx, y+dy), (dx, dy))


def walk(grid, robot, instructions, part):

    for instruction in instructions:

        dx, dy = directions[instruction]

        next_x, next_y = robot.x + dx, robot.y + dy

        if grid[next_x][next_y] == "#":
            continue

        elif (
            grid[next_x][next_y] == "[" or grid[next_x][next_y] == "]" or grid[next_x][next_y] == "O"
        ):
            find = find_free_spot(grid, robot.x, robot.y, instruction, part)
            if find:
                grid = find
                grid[robot.x][robot.y] = "."
                robot.step(next_x, next_y)
                grid[robot.x][robot.y] = "@"

        elif grid[next_x][next_y] == ".":
            grid[robot.x][robot.y] = "."
            robot.step(next_x, next_y)
            grid[robot.x][robot.y] = "@"

    print(eval(grid, part))


def format_lines(lines):

    lines = lines.replace("#", "##")
    lines = lines.replace("O", "[]")
    lines = lines.replace(".", "..")
    lines = lines.replace("@", "@.")

    return lines


def run(part):

    with open("input.txt", 'r') as file:
        lines = file.read()

    lines = lines.split("\n\n")

    if part == "part2":
        lines[0] = format_lines(lines[0])

    grid = [[char for char in line.strip()] for line in lines[0].split("\n") if line.strip()]
    
    x, y = next(((r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == '@'), None)

    walk(grid, Robot(x, y), lines[1].replace("\n", ""), part)


run(part="part1")
run(part="part2")
from enum import Enum


class Direction(Enum):

    HorizontallyLeft = (0, -1)
    HorizontallyRight = (0, 1)

    VerticallyUp = (-1, 0)
    VerticallyDown = (1, 0)

    DiagonallyLeftUp = (-1, -1)
    DiagonallyRightUp = (-1, 1)
    DiagonallyLeftDown = (1, -1)
    DiagonallyRightDown = (1, 1)


def find_word_count(row, col, grid, word, max_depth, depth=0, direction=None):

    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != word[depth]:
        return 0

    if depth == max_depth:
        return 1

    directions = [
        Direction.HorizontallyLeft, Direction.HorizontallyRight,
        Direction.VerticallyUp, Direction.VerticallyDown,
        Direction.DiagonallyLeftUp, Direction.DiagonallyRightUp,
        Direction.DiagonallyLeftDown, Direction.DiagonallyRightDown
    ]
    
    count = 0
    if depth == 0:
        for direction in directions:
            new_row, new_col = row + direction.value[0], col + direction.value[1]
            count += find_word_count(new_row, new_col, grid, word, max_depth, depth+1, direction)
    else:
        new_row, new_col = row + direction.value[0], col + direction.value[1]
        count += find_word_count(new_row, new_col, grid, word, max_depth, depth+1, direction)

    return count


def P1():

    with open("input.txt", "r") as file:
        grid = [list(line.strip()) for line in file]

    word = "XMAS"
    max_depth = len(word)-1

    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            count += find_word_count(row, col, grid, word, max_depth)

    print(count)


def correct_pattern(square):

    if ((square[0][0] == "M" and square[1][1] == "A" and square[2][2] == "S" or
        square[0][0] == "S" and square[1][1] == "A" and square[2][2] == "M") and
       (square[0][2] == "M" and square[1][1] == "A" and square[2][0] == "S" or
        square[0][2] == "S" and square[1][1] == "A" and square[2][0] == "M")):
        return True
    
    return False


def P2():

    with open("input.txt", "r") as file:
        grid = [list(line.strip()) for line in file]

    count = 0

    for r in range(len(grid) - 2):
        for c in range(len(grid[0]) - 2): 
            square = [row[c:c+3] for row in grid[r:r+3]]
            
            count += correct_pattern(square)

    print(count)


P1()
P2()
def sides(region):

    corners = 0

    directions = [
        (-1, 0, 0, -1), 
        (-1, 0, 0, 1),   
        (1, 0, 0, -1),   
        (1, 0, 0, 1)    
    ]

    for row, column in region:

        for dx1, dy1, dx2, dy2 in directions:

            if (
                (row+dx1, column+dy1) in region and
                (row+dx2, column+dy2) in region and
                (row+dx1, column+dy2) not in region
            ):
                corners += 1

        neighbors = []
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            if (row+dx, column+dy) in region:
                neighbors.append((row+dx, column+dy))

        if len(neighbors) == 0:
            corners += 4
            continue
        elif len(neighbors) == 1:
            corners += 2
            continue

        if (
            not any(r >= row and c <= column for r, c in neighbors) or  
            not any(r <= row and c <= column for r, c in neighbors) or  
            not any(r <= row and c >= column for r, c in neighbors) or   
            not any(r >= row and c >= column for r, c in neighbors)
        ):
            corners += 1

    return corners


def dfs(row, column, plot, visited):

    if not (0 <= row < len(grid) and 0 <= column < len(grid[0])) or grid[row][column] != plot:
        return 0, 1 

    if (row, column) in visited:
        return 0, 0

    visited.add((row, column))

    area, fences = 1, 0

    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        next_area, next_fences = dfs(row + dx, column + dy, plot, visited)
        area += next_area
        fences += next_fences

    return area, fences


def run(grid):

    cost_p1 = 0
    cost_p2 = 0

    visited = set()

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if (row, column) in visited:
                continue

            store = visited.copy()

            area, fences = dfs(row, column, grid[row][column], visited)

            cost_p1 += area * fences  
            cost_p2 += area * sides(list(visited - store))

    print(cost_p1)
    print(cost_p2)


with open("input.txt", "r") as file:
    grid = [[str(digit) for digit in line.strip()] for line in file]

run(grid)
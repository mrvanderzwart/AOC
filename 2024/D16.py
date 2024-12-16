import heapq


DIRS = [
    (0, 1), (1, 0), (0, -1), (-1, 0)
]


def walk(grid, row, column, target):

    Q = []

    heapq.heappush(Q, (0, row, column, 0))

    if target == "S":
        heapq.heappush(Q, (0, row, column, 1))
        heapq.heappush(Q, (0, row, column, 2))
        heapq.heappush(Q, (0, row, column, 3))

    visited = set()

    distance_matrix = {}

    while Q:

        cost, row, column, dir = heapq.heappop(Q)

        key = (row, column, dir if target == "S" else (dir + 2) % 4)
        distance_matrix[key] = min(distance_matrix.get(key, float('inf')), cost)

        if grid[row][column] == target:
            break

        if (
            (row, column, dir) in visited
        ):
            continue

        visited.add((row, column, dir))

        dx, dy = DIRS[dir]

        if grid[row+dx][column+dy] != "#":
            heapq.heappush(Q, (cost+1, row+dx, column+dy, dir))

        heapq.heappush(Q, (cost+1000, row, column, (dir+1)%4))

        heapq.heappush(Q, (cost+1000, row, column, (dir+3)%4))

    return distance_matrix, cost


def find_tiles(grid, distance_matrix_1, distance_matrix_2, cost):

    count = 0

    for row in range(len(grid)):  
        for col in range(len(grid[row])):  
            if grid[row][col] != "#":
                tuples1 = [key for key, _ in distance_matrix_1.items() if key[0] == row and key[1] == col]
                tuples2 = [key for key, _ in distance_matrix_2.items() if key[0] == row and key[1] == col]

                for tuple in tuples2:

                    if tuple in tuples1 and (distance_matrix_1[tuple] + distance_matrix_2[tuple] == cost):
                        count += 1
                        break

    print(count)


def run():

    with open("input.txt", "r") as file:
        grid = [[str(digit) for digit in line.strip()] for line in file]

    r, c = next(((r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == 'S'), None)

    distance_matrix_1, cost = walk(grid, r, c, "E")

    print(cost)

    r, c = next(((r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == 'E'), None)

    distance_matrix_2, _ = walk(grid, r, c, "S")

    find_tiles(grid, distance_matrix_1, distance_matrix_2, cost)


run()
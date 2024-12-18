import heapq


def shortest_path(grid):

    Q = []

    heapq.heappush(Q, (0, 0, 0))

    visited = set()

    while Q:

        cost, row, column = heapq.heappop(Q)

        if row == 70 and column == 70:
            return cost

        if (row, column) in visited:
            continue

        visited.add((row, column))

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if (
                0 <= row+dx <= 70 and
                0 <= column+dy <= 70 and
                grid[row+dx][column+dy] != "#"
            ):
                heapq.heappush(Q, (cost+1, row+dx, column+dy))


def P1(grid, byte_list):

    for (row, column) in byte_list:
        grid[row][column] = "#"

    print(shortest_path(grid))


def P2(grid, byte_list):

    for (row, column) in byte_list:
        grid[row][column] = "#"

        if shortest_path(grid) is None:
            print(f"{column},{row}")
            break


def run():

    grid = [["." for _ in range(70+1)] for _ in range(70+1)]

    byte_list = []

    with open("input.txt", "r") as file:
        for line in file:

            line = line.split(",")
            column, row = int(line[0]), int(line[1])

            byte_list.append((row, column))

    P1(grid, byte_list[:1024])
    P2(grid, byte_list)


run()
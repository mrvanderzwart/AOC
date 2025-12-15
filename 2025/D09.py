import matplotlib.pyplot as plt

from itertools import combinations


area = lambda x, y: (abs(x[0] - y[0]) + 1) * (abs(x[1] - y[1]) + 1)


def check_red_green(rectangle, red_tiles, green_tiles):

    x_start = min(rectangle[0][0], rectangle[1][0])
    y_start = min(rectangle[0][1], rectangle[1][1])
    x_end = max(rectangle[0][0], rectangle[1][0])
    y_end = max(rectangle[0][1], rectangle[1][1])

    for x in range(x_start, x_end + 1):
        for y in range(y_start, y_end + 1):
            if (x, y) not in red_tiles and (x, y) not in green_tiles:
                return False
            
    return True


def compress_grid(red_tiles):

    unique_x = sorted(set(x for x, y in red_tiles))
    unique_y = sorted(set(y for x, y in red_tiles))

    x_mapping = {x: i for i, x in enumerate(unique_x)}
    y_mapping = {y: i for i, y in enumerate(unique_y)}

    compressed_tiles = set((x_mapping[x], y_mapping[y]) for x, y in red_tiles)

    x_mapping = {i: x for x, i in x_mapping.items()}
    y_mapping = {i: y for y, i in y_mapping.items()}

    return compressed_tiles, x_mapping, y_mapping


def flood_fill(green_tiles, red_tiles, start=(125, 125)):

    stack = [start]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        x, y = stack.pop()

        if (x, y) in green_tiles or (x, y) in red_tiles:
            continue

        green_tiles.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            stack.append((nx, ny))


def get_green_tiles(rectangles, red_tiles):

    green_tiles = set()

    for red_tile1, red_tile2 in rectangles:
            
        x, y = red_tile1
        u, v = red_tile2

        if x == u:
            for i in range(min(y, v) + 1, max(y, v)):
                green_tiles.add((x, i))
        elif y == v:
            for i in range(min(x, u) + 1, max(x, u)):
                green_tiles.add((i, y))

    flood_fill(green_tiles, red_tiles)

    return green_tiles


def plot(red_tiles):

    red_x = [col for row, col in red_tiles]
    red_y = [row for row, col in red_tiles]

    plt.scatter(red_x, red_y, color='red')

    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    ax.invert_yaxis()

    ax.grid(True)

    plt.show()


def parse_input():
    
    with open("input.txt") as f:
        lines = f.readlines()

    red_tiles = []

    for line in lines:
        numbers = line.strip().split(',')
        red_tiles.append((int(numbers[1]), int(numbers[0])))

    return red_tiles


def P1(red_tiles):

    rectangles = list(combinations(red_tiles, 2))

    rectangles_lengths = [(area(x, y), (x, y)) for x, y in rectangles]
    rectangles_lengths = sorted(rectangles_lengths, key=lambda item: item[0], reverse=True)

    print(rectangles_lengths[0][0])


def P2(red_tiles, plotting=False):

    compressed_red_tiles, x_mapping, y_mapping = compress_grid(red_tiles)

    if plotting:
        plot(red_tiles=compressed_red_tiles)
        return

    rectangles = list(combinations(compressed_red_tiles, 2))

    green_tiles = get_green_tiles(rectangles, compressed_red_tiles)

    rectangles_lengths = [(area((x_mapping[u[0]], y_mapping[u[1]]), (x_mapping[v[0]], y_mapping[v[1]])), (u, v)) for u, v in rectangles]
    rectangles_lengths = sorted(rectangles_lengths, key=lambda item: item[0], reverse=True)

    for rectangle in rectangles_lengths:
        if check_red_green(rectangle[1], compressed_red_tiles, green_tiles):
            print(rectangle[0])
            break


red_tiles = parse_input()

P1(red_tiles)
P2(red_tiles)
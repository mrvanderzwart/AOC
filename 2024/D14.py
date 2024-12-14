import itertools
import re


WIDTH = 101
HEIGHT = 103


class Robot:

    def __init__(self, px, py, vx, vy):

        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy


    def step(self):

        self.px = (self.px + self.vx) % WIDTH
        self.py = (self.py + self.vy) % HEIGHT


def count(robots):

    middle_v = WIDTH // 2
    middle_h = HEIGHT // 2

    return (
        sum(1 for robot in robots if robot.px < middle_v and robot.py < middle_h) *
        sum(1 for robot in robots if robot.px > middle_v and robot.py < middle_h) *
        sum(1 for robot in robots if robot.px < middle_v and robot.py > middle_h) *
        sum(1 for robot in robots if robot.px > middle_v and robot.py > middle_h)
    )


def display(robots):

    grid = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for robot in robots:
        grid[robot.py][robot.px] = "X"

    print("\n\n")
    for row in grid:
        print("".join(map(str, row)))
    print("\n\n")


def count_robots(robots):

    count = 0
    offset = WIDTH / 4

    for robot in robots:

        if (
            offset < robot.px < WIDTH-offset and
            offset < robot.py < HEIGHT-offset
        ):
            count += 1

    return count


def run():

    with open("input.txt", 'r') as file:
        lines = file.readlines()

    robots = []
    
    for line in lines:
        match = re.search(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)
        px, py, vx, vy = map(int, match.groups())
        robots.append(Robot(px, py, vx, vy))

    for second in itertools.count(1):
        for robot in robots:
            robot.step()

        if second == 100:
            print(f"P1: {count(robots)}")

        score = count_robots(robots)

        if score > len(robots) / 2:
            display(robots)
            print(f"P2: {second}")
            break


run()
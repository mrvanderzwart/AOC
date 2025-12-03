import re


def read_lines(path: str = 'input.txt') -> list:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()


def P1(lines, dial=50, password=0): 

    for line in lines:
        rotation = int(re.search(r"\d+", line).group())
        direction = -1 if 'L' in line else 1
        
        dial = (dial + direction * rotation) % 100

        if dial == 0:
            password += 1

    print(password)


def P2(lines, dial=50, password=0):
    
    for line in lines:
        rotation = int(re.search(r"\d+", line).group())
        direction = -1 if 'L' in line else 1

        password += rotation // 100

        if (
            direction == -1 and dial - (rotation % 100) <= 0 and dial != 0 or
            direction == 1 and dial + (rotation % 100) >= 100 and dial != 100
        ):
            password += 1

        dial = (dial + direction * rotation) % 100

    print(password)


lines = read_lines()

P1(lines)
P2(lines)
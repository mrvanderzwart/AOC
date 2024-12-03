import re


def P1():

    with open("input.txt", "r") as file:
        content = file.read()

    pattern = r"mul\((\d+),\s*(\d+)\)"

    matches = re.findall(pattern, content)

    total_sum = sum(int(x) * int(y) for x, y in matches)

    print(total_sum)


def P2():

    with open("input.txt", "r") as file:
        content = file.read()

    pattern_between = r"don't\(\).*?do\(\)"
    content = re.sub(pattern_between, '', content, flags=re.DOTALL)

    pattern_after = r"(?<=don't\(\))(?!.*do\(\)).*"
    content = re.sub(pattern_after, '', content, flags=re.DOTALL)

    pattern = r"mul\((\d+),\s*(\d+)\)"

    matches = re.findall(pattern, content)

    total_sum = sum(int(x) * int(y) for x, y in matches)

    print(total_sum)


P1()
P2()
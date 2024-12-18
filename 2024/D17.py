import re

from z3 import *


def P1(registers):

    a, b, c = registers["A"], registers["B"], registers["C"]

    output = ""

    while a != 0:
        b = a % 8
        b = int(b ^ 1)
        c = int(a / (1 << b))
        a = int(a / (1 << 3))
        b = int(b ^ c)
        b = int(b ^ 6)
        output += f"{b % 8},"

    print(output[:-1])


def P2(numbers):

    conditions = Optimize()
    x = BitVec('x', 64)
    a, b, c = x, 0, 0
    for output in numbers:
        b = a % 8
        b = b ^ 1
        c = a / (1 << b)
        a = a / (1 << 3)
        b = b ^ c
        b = b ^ 6
        conditions.add((b % 8) == output)

    conditions.add(a == 0)
    conditions.minimize(x)
    conditions.check()
    print(conditions.model().eval(x))


def run():

    with open("input.txt", "r") as file:
        content = file.read()

    register_lines, program_line = content.split("\n\n")

    registers = {}

    register_lines = register_lines.split("\n")

    match = re.search(r'Register A: (-?\d+)', register_lines[0])
    registers["A"] = int(match.group(1))

    match = re.search(r'Register B: (-?\d+)', register_lines[1])
    registers["B"] = int(match.group(1))

    match = re.search(r'Register C: (-?\d+)', register_lines[2])
    registers["C"] = int(match.group(1))

    numbers = list(map(int, program_line.split(":")[1].split(",")))

    P1(registers)
    P2(numbers)


run()
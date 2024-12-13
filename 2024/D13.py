import re
import sympy as s


def get_tokens(data):

    A = s.symbols("A")
    B = s.symbols("B")

    eq1_left = (data["Prize"][0] - A * data["A"][0]) / data["B"][0]
    eq1_right = (data["Prize"][1] - A * data["A"][1]) / data["B"][1]

    equation = s.Eq(eq1_left, eq1_right)

    press_A = s.solve(equation, A)[0]

    eq1_left = (data["Prize"][0] - B * data["B"][0]) / data["A"][0]
    eq1_right = (data["Prize"][1] - B * data["B"][1]) / data["A"][1]

    equation = s.Eq(eq1_left, eq1_right)

    press_B = s.solve(equation, B)[0]

    if (
        not isinstance(press_A, s.core.numbers.Integer) or
        not isinstance(press_B, s.core.numbers.Integer)
    ):
        return 0

    return 3 * press_A + press_B


def run(part):

    with open("input.txt", 'r') as file:
        content = file.read()
    
    blocks = content.strip().split('\n\n')

    tokens = 0
    constant = 0

    if part == "part2":
        constant = 10000000000000
    
    for block in blocks:

        match_a = re.search(r'Button A: X\+(\d+), Y\+(\d+)', block)
        match_b = re.search(r'Button B: X\+(\d+), Y\+(\d+)', block)
        match_prize = re.search(r'Prize: X=(\d+), Y=(\d+)', block)
        
        if match_a and match_b and match_prize:
            data = {
                'A': (int(match_a.group(1)), int(match_a.group(2))),
                'B': (int(match_b.group(1)), int(match_b.group(2))),
                'Prize': (int(match_prize.group(1))+constant, int(match_prize.group(2))+constant),
            }

            tokens += get_tokens(data)

    print(tokens)


run("part1")
run("part2")
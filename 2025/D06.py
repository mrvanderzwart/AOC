def parse_input():

    with open('input.txt', 'r') as f:
        lines = f.readlines()

    ops = [ch for ch in lines[-1] if ch in ['+', '*']]

    return lines[:-1], ops


def P1(lines, ops):

    sum_numbers = []
    
    for line in lines:
        for index, number in enumerate(line.strip().split()):

            if index == len(sum_numbers):
                sum_numbers.append(int(number))
            else:
                if ops[index] == '+':
                    sum_numbers[index] += int(number)
                elif ops[index] == '*':
                    sum_numbers[index] *= int(number)

    print(sum(sum_numbers))


def P2(lines, ops, total=0):

    transposed = list(zip(*lines))
    result = ["".join(row).rstrip() for row in transposed]
    
    index = 0
    number = 0

    for ch in result:

        if ch == '':
            index += 1
            total += number
            number = 0
            continue
        
        new_num = int(ch.strip())

        if ops[index] == '+':
            number += new_num
        elif ops[index] == '*':
            number = new_num if number == 0 else number * new_num

    print(total)


lines, ops = parse_input()

P1(lines, ops)
P2(lines, ops)
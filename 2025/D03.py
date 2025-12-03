

def read_lines(path: str = 'input.txt') -> list:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()
    

def P1(lines, total=0):

    for line in lines:

        num1 = int(line[0])
        num2 = 0

        for index, digit in enumerate(line[1:]):
            digit = int(digit)
            if digit > num1 and index != len(line) - 2:
                num1 = digit
                num2 = 0
            elif digit > num2:
                num2 = digit

        total += (num1 * 10 + num2)

    print(total)


def P2(lines, total=0, k=12):
    for line in lines:
        next_num = [0] * k

        for idx, char in enumerate(line):
            digit = int(char)
            remaining = len(line) - idx - 1

            for i in range(k):
                if digit > next_num[i] and remaining >= k - i - 1:
                    next_num[i] = digit

                    for j in range(i + 1, k):
                        next_num[j] = 0
                    break

        new_sum = int("".join(map(str, next_num)))
        total += new_sum

    print(total)


lines = read_lines()
P1(lines)
P2(lines)
from itertools import product


def generate_combinations(numbers, result, operations):
    
    for ops in product(operations, repeat=len(numbers) - 1):

        ops = list(ops)

        total = numbers[0]

        for index in range(len(numbers)-1):

            if total > result:
                break

            if ops[index] == "*":
                total *= numbers[index+1]
            elif ops[index] == "+":
                total += numbers[index+1]
            elif ops[index] == "||":
                total = int(str(total)+str(numbers[index+1]))

        if total == result:
            return result

    return 0


def P1(ops):

    count = 0

    with open("input.txt", "r") as file:
        for line in file:
            result, numbers = line.split(":")
            numbers = list(map(int, numbers.split()))

            count += generate_combinations(numbers, int(result), ops)

    print(count)


P1(ops=["+", "*"])
P1(ops=["+", "*", "||"])
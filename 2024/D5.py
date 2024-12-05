def check_ordering(row, rules):
            
    return all(row[i] not in rules.get(row[j], []) for i in range(len(row)-1) for j in range(i+1, len(row)))


def fix_ordering(row, rules):

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(row) - 1):
            for j in range(i + 1, len(row)):
                if row[j] in rules and row[i] in rules[row[j]]:
                    row[i], row[j] = row[j], row[i]
                    swapped = True 

    return row


def P1(rows, rules):

    total_sum = sum(row[len(row)//2] for row in rows if check_ordering(row, rules))
    print(total_sum)


def P2(rows, rules):

    total_sum = 0

    for row in rows:

        if not check_ordering(row, rules):
            row = fix_ordering(row, rules)
            index = len(row) // 2
            total_sum += row[index]

    print(total_sum)


def parse_input():

    with open("input.txt", "r") as file:
        data = file.read()

    lines = data.strip().split("\n\n")

    rules = {}
    for line in lines[0].splitlines():
        key, value = map(int, line.split("|"))

        if key not in rules:
            rules[key] = []

        rules[key].append(value)

    rows = []
    for line in lines[1].splitlines():
        rows.append(list(map(int, line.split(","))))

    return rows, rules


rows, rules = parse_input()

P1(rows, rules)
P2(rows, rules)
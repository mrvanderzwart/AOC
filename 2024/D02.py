def is_safe_p1(row: list) -> bool:

    reversed_row = row[::-1]
    sorted_row = sorted(row)

    if sorted_row != row and sorted_row != reversed_row:
        return False

    all_differ_by_3 = all(abs(sorted_row[i] - sorted_row[i + 1]) >= 1 and 
                        abs(sorted_row[i] - sorted_row[i + 1]) <= 3 for i in range(len(sorted_row) - 1)
                    )

    if all_differ_by_3:
        return True
    
    return False


def is_safe_p2(row: list, index: int, old_row: list) -> bool:

    reversed_row = row[::-1]
    sorted_row = sorted(row)

    if sorted_row != row and sorted_row != reversed_row:
        if index < len(old_row):
            row = old_row.copy()
            row.pop(index)
            return is_safe_p2(row, index+1, old_row)
        
        return False

    all_differ_by_3 = all(abs(sorted_row[i] - sorted_row[i + 1]) >= 1 and 
                        abs(sorted_row[i] - sorted_row[i + 1]) <= 3 for i in range(len(sorted_row) - 1)
                    )

    if all_differ_by_3:
        return True
    elif index < len(old_row):
        row = old_row.copy()
        row.pop(index)
        return is_safe_p2(row, index+1, old_row)
    
    return False


def P1():

    total_safe = 0

    with open("input.txt", "r") as file:
        for line in file:
            row = list(map(int, line.split()))

            if is_safe_p1(row):
                total_safe += 1

    print(total_safe)


def P2():
    
    total_safe = 0

    with open("input.txt", "r") as file:
        for line in file:
            row = list(map(int, line.split()))

            if is_safe_p2(row, 0, row):
                total_safe += 1

    print(total_safe)


P1()
P2()

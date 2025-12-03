

def read_lines(path: str = 'input.txt') -> list:
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read().strip().split(',')

    return lines


def parts_equal(s: str, sec_length: int) -> bool:

    if len(s) % sec_length != 0:
        return False
    
    part_length = len(s) // sec_length
    part = s[:part_length]
    for i in range(part_length, len(s), part_length):
        if s[i:i + part_length] != part:
            return False
    return True


def P1(lines, invalids=0):

    for line in lines:
        
        numbers = line.split('-')

        for i in range(int(numbers[0]), int(numbers[1]) + 1):
            if parts_equal(str(i), 2):
                invalids += int(i)

    return invalids


def P2(lines, invalids=0):

    for line in lines:
        
        numbers = line.split('-')

        for i in range(int(numbers[0]), int(numbers[1]) + 1):
            for sec_length in range(2, len(str(i)) + 1):
                if parts_equal(str(i), sec_length):
                    invalids += int(i)
                    break

    return invalids


lines = read_lines()
print(P1(lines))
print(P2(lines))
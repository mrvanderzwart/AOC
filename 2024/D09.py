def get_memory():

    with open("input.txt", "r") as file:
        input_data = file.read()

    max_idx = len(input_data) // 2

    disk_map = list(map(int, input_data.strip()))
    memory = []
    hole_list = {}

    index = 0
    for i in range(len(disk_map)):
        if i % 2 == 0:
            memory += [index] * disk_map[i]
            index += 1
        else:
            hole_start = len(memory)
            hole_list[hole_start] = disk_map[i]
            memory += ['.'] * disk_map[i]

    return memory, max_idx, hole_list  


def P1():

    memory, _, _ = get_memory()

    total_memory = len(memory)
    for i, idx in enumerate(reversed(memory)):
        rev_index = total_memory - 1 - i
        if idx != ".":
            free_idx = memory.index(".")
            if free_idx != -1 and free_idx < rev_index:
                memory[free_idx], memory[rev_index] = memory[rev_index], memory[free_idx]
            else:
                break

    check_sum = sum(i * int(mem) for i, mem in enumerate(memory) if mem != '.')
    
    print(check_sum)


def P2():

    memory, max_idx, hole_list = get_memory()

    for index in range(max_idx, 0, -1):

        idx_count = memory.count(index)

        hole = min((k for k, v in hole_list.items() if v >= idx_count), default=None)

        if hole and hole < memory.index(index):
            memory = list(map(lambda x: '.' if x == index else x, memory))
            for hole_index in range(hole, hole+idx_count):
                memory[hole_index] = index

            new_index = hole + idx_count

            hole_list[new_index] = hole_list[hole] - idx_count

            hole_list.pop(hole)

    check_sum = sum(i * int(mem) for i, mem in enumerate(memory) if mem != '.')

    print(check_sum)

P1()
P2()

def merge_ranges(ranges):

    ranges = sorted(ranges, key=lambda r: r[0])

    merged = [list(ranges[0])]
    for start, end in ranges[1:]:

        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return [tuple(r) for r in merged]


def P1(ranges, ids, n_fresh=0):

    for id in ids:
        n_fresh += any(n_start <= int(id) and n_end >= int(id) for n_start, n_end in ranges)

    print(n_fresh)


def P2(ranges, fresh=0):

    merged_ranges = merge_ranges(ranges)

    for n_start, n_end in merged_ranges:
        fresh += n_end - n_start + 1

    print(fresh)


def parse_input():
    
    with open('input.txt', 'r') as f:
        sections = f.read().strip().split('\n\n')

    ranges = []

    for line in sections[0].split('\n'):
        new_numbers = line.split('-')   
        ranges.append((int(new_numbers[0]), int(new_numbers[1])))

    return ranges, sections

ranges, sections = parse_input()

P1(ranges, sections[1].split('\n'))
P2(ranges)
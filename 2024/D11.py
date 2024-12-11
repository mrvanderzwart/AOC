import time

def blink(count, stone, depth, total_blinks, cache):

    count = 1

    if depth == total_blinks:
        return count
    
    if (stone, depth) in cache:
        return cache[(stone, depth)]

    if stone == "0":
        result = blink(count, "1", depth+1, total_blinks, cache)
    elif len(stone)%2 == 0:
        stone_len = len(stone)//2
        left = int(stone[:stone_len])
        right = int(stone[stone_len:])

        count += 1
        
        result = (
            blink(count, str(left), depth+1, total_blinks, cache) + 
            blink(count, str(right), depth+1, total_blinks, cache)
        )
    else:
        result = blink(count, str(int(stone) * 2024), depth+1, total_blinks, cache)
    
    cache[(stone, depth)] = result
    
    return result


def run():

    with open("input.txt", 'r') as file:
        stones = list(map(str, file.read().split()))

    count_p1, count_p2 = 0, 0

    for stone in stones:
        count_p1 += blink(0, stone, 0, 25, {})
        count_p2 += blink(0, stone, 0, 75, {})

    print(f"P1: {count_p1}")
    print(f"P2: {count_p2}")


run()
import bisect


def P1():

    with open("input.txt", "r") as file:

        left = []
        right = []

        for line in file:
            numbers = list(map(int, line.split()))
            
            bisect.insort(left, numbers[0])
            bisect.insort(right, numbers[1])

        total_distance = 0

        for index in range(len(left)):
            total_distance += abs(left[index] - right[index])

        print(total_distance)


def P2():
    
    with open("input.txt", "r") as file:

        left = []
        right = {}

        for line in file:
            numbers = list(map(int, line.split()))
            
            left.append(numbers[0])
            
            if numbers[1] not in right:
                right[numbers[1]] = 1
            else:
                right[numbers[1]] += 1

        similarity_score = 0

        for index in range(len(left)):

            if left[index] not in right:
                continue

            similarity_score += (left[index] * right[left[index]])

        print(similarity_score)


P1()
P2()
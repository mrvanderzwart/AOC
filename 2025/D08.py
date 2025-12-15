from collections import defaultdict


class UnionFind:
    def __init__(self, size):
      
        self.parent = list(range(size))
    
    def find(self, i):
      
        if self.parent[i] == i:
            return i
          
        return self.find(self.parent[i])
    
    def unite(self, i, j):
      
        irep = self.find(i)
        jrep = self.find(j)
        
        self.parent[irep] = jrep


def parse_input():

    with open("input.txt") as f:
        lines = f.readlines()

    number_list = []

    for line in lines:
        numbers = line.split(',')
        number_list.append([int(number) for number in numbers])

    sums = {}

    for idx, x in enumerate(number_list):
        for idy, y in enumerate(number_list):
            if idy > idx:
                sums[(idx, idy)] = pow(x[0] - y[0], 2) + pow(x[1] - y[1], 2) + pow(x[2] - y[2], 2)

    ordered_sums = sorted(sums.items(), key=lambda item: item[1])

    return number_list, ordered_sums


def P1(number_list, ordered_sums):
                    
    uf = UnionFind(len(number_list))

    for i in ordered_sums[:1000]:
        uf.unite(i[0][0], i[0][1])

    sets = defaultdict(list)
    for i in range(len(uf.parent)):
        sets[uf.find(i)].append(i)

    largest_three_sets = sorted(sets.values(), key=len, reverse=True)[:3]

    lengths = len(largest_three_sets[0])
    for s in largest_three_sets[1:]:
        lengths *= len(s)

    print(lengths)


def P2(number_list, ordered_sums):
  
    uf = UnionFind(len(number_list))

    for i in ordered_sums:

        uf.unite(i[0][0], i[0][1])

        sets = defaultdict(list)
        for j in range(len(uf.parent)):
            sets[uf.find(j)].append(j)

        if len(sets) == 1:
            print(number_list[i[0][0]][0] * number_list[i[0][1]][0])
            break


number_list, ordered_sums = parse_input()

P1(number_list, ordered_sums)
P2(number_list, ordered_sums)
from collections import defaultdict
from itertools import product, combinations, permutations

with open('../input.txt', 'r') as file:
    data = file.read().splitlines()


startp = defaultdict(tuple)

for c in range(len(data[0])):
    if (data[0][c] == "."):
        startp[0] = (0, c)


for y in range(len(data)):
    for x in range(len(data[y])):
        if (data[y][x] == "E" and x > 3):
            startp[1] = (y, x)
        elif (data[y][x] == "R" and x < len(data[y]) - 4):
            startp[2] = (y, x)

def dijkstra(grid, start, end):
    queue = [(0, start)]
    seen = set()
    while queue:
        cost, pos = queue.pop(0)
        if pos in seen:
            continue
        seen.add(pos)
        y, x = pos
        if y == end[0] and x == end[1]:
            return cost
        if grid[y][x] == "#" or grid[y][x] == "~":
            continue
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if 0 <= y + dy < len(grid) and 0 <= x + dx < len(grid[0]):
                queue.append((cost + 1, (y + dy, x + dx)))
    return float("inf")

plants = defaultdict(list)

plants[0] = defaultdict(set)
plants[1] = defaultdict(set)
plants[2] = defaultdict(set)

for i in range(len(data)):
    for c in range(len(data[i])):
        if (data[i][c] not in ["#", "~", "."]):
            key = 0
            if data[i][c] in "ABCDE":
                key = 1
            elif data[i][c] in "GHIJK":
                key = 0
            elif data[i][c] in "NOPQR":
                key = 2

            if data[i][c] == "K":
                plants[key][str(c)+data[i][c]].add((i, c)) # K is a "special" case
            else:
                plants[key][data[i][c]].add((i, c))

dplants = plants
total = 0
for i in range(len(dplants)):

    plants = dplants[i]

    pair_combinations = []
    plant_types = list(plants.keys())

    plant_pairs = list(combinations(plant_types, 2))

    for type1, type2 in plant_pairs:
        positions1 = plants[type1]
        positions2 = plants[type2]
        pair_combinations.extend(list(product(positions1, positions2)))

    costs = defaultdict(dict)

    ys, xs = startp[i]

    for plantsl in plants:
        for plant in plants[plantsl]:
            cost = dijkstra(data, (ys,xs), plant)
            costs[(ys,xs)][plant] = cost
            costs[plant][(ys,xs)] = cost

    for pair in pair_combinations:
        start = pair[0]
        end = pair[1]
        cost = dijkstra(data, start, end)
        costs[start][end] = cost
        costs[end][start] = cost

    all_combinations = []
    plant_types = list(plants.keys())

    plant_orders = list(permutations(plant_types))

    for order in plant_orders:
        positions_in_order = [plants[plant] for plant in order]
        order_combinations = list(product(*positions_in_order))
        all_combinations.extend(order_combinations)

    min_cost = float("inf")
    for order in all_combinations:
        cost = costs[(ys, xs)][order[0]]
        for i in range(len(order) - 1):
            cost += costs[order[i]][order[i + 1]]
        cost += costs[order[-1]][(ys, xs)]
        min_cost = min(min_cost, cost)

    total += min_cost

print(total+6+6) # 6*2 for the 6 steps between each route to middle
from collections import defaultdict
from itertools import product, combinations, permutations

with open('../input.txt', 'r') as file:
    data = file.read().splitlines()

ys,xs = 0,0


for i in range(len(data)):
    if (i == 0 or i == len(data) - 1):
        for c in range(len(data[i])):
            if (data[i][c] == "."):
                xs = c
                ys = i
                break
    else:
        if (data[i][0] == "."):
            xs = 0
            ys = i
            break
        elif (data[i][len(data[i]) - 1] == "."):
            xs = len(data[i]) - 1
            ys = i
            break

plants = defaultdict(set)

for i in range(len(data)):
    for c in range(len(data[i])):
        if (data[i][c] not in ["#", "~", "."]):
            plants[data[i][c]].add((i, c))

plants = defaultdict(set)
for i in range(len(data)):
    for c in range(len(data[i])):
        if (data[i][c] not in ["#", "~", "."]):
            plants[data[i][c]].add((i, c))

pair_combinations = []
plant_types = list(plants.keys())

plant_pairs = list(combinations(plant_types, 2))

for type1, type2 in plant_pairs:
    positions1 = plants[type1]
    positions2 = plants[type2]
    pair_combinations.extend(list(product(positions1, positions2)))

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

costs = defaultdict(dict)

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

print(min_cost)
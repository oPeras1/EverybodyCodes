from math import inf

moves = []
with open("../input.txt") as f:
    for line in f:
        moves.append(line.strip().split(","))

visited = set()

def update_positions(start, end, coord_index, current):
    step = 1 if start < end else -1
    for i in range(start + step, end + step, step):
        pos = list(current)
        pos[coord_index] = i
        visited.add(tuple(pos))

ends = []

for movet in moves:
    current = [0, 0, 0]
    for i in range(len(movet)):
        move = movet[i]
        direction = move[0]
        distance = int(move[1:])
        old = current[:]

        if direction == "U":
            current[0] += distance
            update_positions(old[0], current[0], 0, current)
        elif direction == "D":
            current[0] -= distance
            update_positions(old[0], current[0], 0, current)
        elif direction == "R":
            current[1] += distance
            update_positions(old[1], current[1], 1, current)
        elif direction == "L":
            current[1] -= distance
            update_positions(old[1], current[1], 1, current)
        elif direction == "F":
            current[2] += distance
            update_positions(old[2], current[2], 2, current)
        elif direction == "B":
            current[2] -= distance
            update_positions(old[2], current[2], 2, current)

        if i == len(movet) - 1:
            ends.append(tuple(current))

trunk = {(i, 0, 0) for i in range(max(visited, key=lambda x: x[0])[0] + 1) if (i, 0, 0) in visited}

location_costs = {end: {loc: 0 if loc == end else inf for loc in visited} for end in ends}

for end, costs in location_costs.items():
    to_update = visited.copy()
    while to_update:
        new_update = set()
        for loc in to_update:
            neighbors = [
                (loc[0] + d[0], loc[1] + d[1], loc[2] + d[2])
                for d in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
                if (loc[0] + d[0], loc[1] + d[1], loc[2] + d[2]) in costs
            ]
            neighbor_costs = map(costs.get, neighbors)
            new_cost = min(neighbor_costs) + 1
            if new_cost < costs[loc]:
                costs[loc] = new_cost
                new_update.update(neighbors)
        to_update = new_update

def murkiness(tap_location):
    return sum(costs[tap_location] for costs in location_costs.values())

min_murkiness = min(map(murkiness, trunk))
print(min_murkiness)

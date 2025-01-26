moves = []
with open("../input.txt") as f:
    for line in f:
        moves.append(line.strip().split(","))

visited = set()

def update_positions(start, end, coord_index):
    step = 1 if start < end else -1
    for i in range(start + step, end + step, step):
        pos = list(current)
        pos[coord_index] = i
        visited.add(tuple(pos))

for movet in moves:
    current = [0, 0, 0]
    for move in movet:
        direction = move[0]
        distance = int(move[1:])
        old = current[:]

        if direction == "U":
            current[0] += distance
            update_positions(old[0], current[0], 0)
        elif direction == "D":
            current[0] -= distance
            update_positions(old[0], current[0], 0)
        elif direction == "R":
            current[1] += distance
            update_positions(old[1], current[1], 1)
        elif direction == "L":
            current[1] -= distance
            update_positions(old[1], current[1], 1)
        elif direction == "F":
            current[2] += distance
            update_positions(old[2], current[2], 2)
        elif direction == "B":
            current[2] -= distance
            update_positions(old[2], current[2], 2)

print(len(visited))

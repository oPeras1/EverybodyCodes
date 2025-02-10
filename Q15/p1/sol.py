with open('../input.txt', 'r') as file:
    data = file.read().splitlines()

y,x = 0,0


for i in range(len(data)):
    if (i == 0 or i == len(data) - 1):
        for c in range(len(data[i])):
            if (data[i][c] == "."):
                x = c
                y = i
                break
    else:
        if (data[i][0] == "."):
            x = 0
            y = i
            break
        elif (data[i][len(data[i]) - 1] == "."):
            x = len(data[i]) - 1
            y = i
            break

def dijkstra(grid, start):
    queue = [(0, start)]
    seen = set()
    while queue:
        cost, pos = queue.pop(0)
        if pos in seen:
            continue
        seen.add(pos)
        y, x = pos
        if grid[y][x] != "." and grid[y][x] != "H":
            continue
        if grid[y][x] == "H":
            return cost
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if 0 <= y + dy < len(grid) and 0 <= x + dx < len(grid[0]):
                queue.append((cost + 1, (y + dy, x + dx)))
    return float("inf")

print(dijkstra(data, (y, x))*2)
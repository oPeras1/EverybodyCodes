from math import inf
from collections import defaultdict, deque
import heapq

with open("../input.txt") as f:
    grid = [list(line.strip()) for line in f]

initial_levels = defaultdict(lambda: defaultdict(int))
start = None
end = None

for i in range(len(grid)):
    for j in range(len(grid[0])):
        cell = grid[i][j]
        if cell == 'S':
            start = (i, j)
            initial_levels[i][j] = 0
        elif cell == 'E':
            end = (i, j)
            initial_levels[i][j] = 0
        elif cell == '#':
            initial_levels[i][j] = inf
        elif cell == " ":
            initial_levels[i][j] = inf
        else:
            initial_levels[i][j] = int(cell)

def dijkstra():
    rows = len(grid)
    cols = len(grid[0])

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start_x, start_y = start

    pq = [(0, start_x, start_y, 0)]
    dist = defaultdict(lambda: inf)
    dist[(start_x, start_y, 0)] = 0

    while pq:
        total_time, x, y, current_level = heapq.heappop(pq)

        if (x, y) == end and current_level == 0:
            print(total_time)
            return

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                neighbor_level = initial_levels[nx][ny]
                if neighbor_level == inf:
                    continue 

                weight = min(abs(neighbor_level - current_level)+1, abs(10-neighbor_level+current_level)+1, abs(10-current_level+neighbor_level)+1)

                if grid[nx][ny] == "S":
                    weight -= 1

                new_time = total_time + weight

                if new_time < dist[(nx, ny, neighbor_level)]:
                    dist[(nx, ny, neighbor_level)] = new_time
                    heapq.heappush(pq, (new_time, nx, ny, neighbor_level))

dijkstra()
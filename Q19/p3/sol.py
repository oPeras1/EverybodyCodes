from copy import deepcopy

with open('../input.txt') as f:
    lines = f.read().splitlines()

loop = list(lines[0])

grid = [list(line) for line in lines[2:]]
n_rows = len(grid)
n_cols = len(grid[0]) if n_rows > 0 else 0

rotation_points = []
for i in range(1, n_rows - 1):
    for j in range(1, n_cols - 1):
        rotation_points.append((i, j))

ops = []
L = len(loop)
for idx, pos in enumerate(rotation_points):
    direction = loop[idx % L]
    ops.append((pos, direction))

def rotate_grid(subgrid, pos, direction):
    y, x = pos
    coords = [(y-1, x-1), (y-1, x), (y-1, x+1),
              (y,   x+1),
              (y+1, x+1), (y+1, x), (y+1, x-1),
              (y,   x-1)]
    old_vals = [subgrid[r][c] for r, c in coords]
    if direction == 'R': 
        new_vals = [old_vals[-1]] + old_vals[:-1]
    elif direction == 'L':  
        new_vals = old_vals[1:] + [old_vals[0]]

    for (r, c), val in zip(coords, new_vals):
        subgrid[r][c] = val


labels = [[r * n_cols + c for c in range(n_cols)] for r in range(n_rows)]

perm_grid = deepcopy(labels)
for pos, direction in ops:
    rotate_grid(perm_grid, pos, direction)

N_cells = n_rows * n_cols
p = [None] * N_cells
for r in range(n_rows):
    for c in range(n_cols):
        orig_label = perm_grid[r][c]
        new_index = r * n_cols + c
        p[orig_label] = new_index


R = 1048576000
p_exp = [None] * N_cells 
visited = [False] * N_cells

for i in range(N_cells):
    if not visited[i]:
        cycle = []
        cur = i
        while not visited[cur]:
            visited[cur] = True
            cycle.append(cur)
            cur = p[cur]
        cycle_len = len(cycle)

        shift = R % cycle_len
        for j, pos in enumerate(cycle):
            p_exp[pos] = cycle[(j + shift) % cycle_len]

final_grid = [[''] * n_cols for _ in range(n_rows)]
for r in range(n_rows):
    for c in range(n_cols):
        orig_index = r * n_cols + c
        final_index = p_exp[orig_index]
        fr, fc = divmod(final_index, n_cols)
        final_grid[fr][fc] = grid[r][c]

phrase_chars = []
found = False
for r in range(n_rows):
    for c in range(n_cols):
        if final_grid[r][c] == '>':
            cy, cx = r, c + 1
            found = True
            break
    if found:
        break

while final_grid[cy][cx] != '<':
    phrase_chars.append(final_grid[cy][cx])
    cx += 1

print("".join(phrase_chars))

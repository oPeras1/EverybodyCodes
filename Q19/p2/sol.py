with open('../input.txt') as f:
    lines = f.read().splitlines()

loop = list(lines[0])

mapping = [list(line) for line in lines[2:]]
n_rows = len(mapping)
n_cols = len(mapping[0]) if mapping else 0

rotation_points = []
for i in range(1, n_rows - 1):
    for j in range(1, n_cols - 1):
        rotation_points.append((i, j))

def rotate(mapp, pos, direction):
    y, x = pos
    coords = [(y-1, x-1), (y-1, x), (y-1, x+1),
              (y,   x+1),
              (y+1, x+1), (y+1, x), (y+1, x-1),
              (y,   x-1)]
    
    vals = [mapp[r][c] for r, c in coords]
    
    if direction == 'R':
        new_vals = [vals[-1]] + vals[:-1]
    elif direction == 'L':
        new_vals = vals[1:] + [vals[0]]
    
    for (r, c), v in zip(coords, new_vals):
        mapp[r][c] = v

n_loop = len(loop)
for _ in range(100):
    for idx, pos in enumerate(rotation_points):
        direction = loop[idx % n_loop]
        rotate(mapping, pos, direction)

start_found = False
for i, row in enumerate(mapping):
    for j, cell in enumerate(row):
        if cell == '>':
            cy, cx = i, j + 1
            start_found = True
            break
    if start_found:
        break

chars = []
while mapping[cy][cx] != '<':
    chars.append(mapping[cy][cx])
    cx += 1

print("".join(chars))

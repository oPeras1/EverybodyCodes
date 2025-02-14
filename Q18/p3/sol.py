from collections import Counter

cells = set()
palms = set()
with open('../input.txt') as f:
    lines = f.read().splitlines()
    height = len(lines)
    width = len(lines[0]) if lines else 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in ('.', 'P'):
                cells.add((y, x))
                if c == 'P':
                    palms.add((y, x))

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs_distances(cells, starts):
    seen = Counter()
    layer = list(starts)
    time = 0
    while layer:
        new_layer = []
        for cell in layer:
            if cell in seen:
                continue
            seen[cell] = time
            for dy, dx in dirs:
                ncell = (cell[0] + dy, cell[1] + dx)
                if ncell in cells and ncell not in seen:
                    new_layer.append(ncell)
        time += 1
        layer = new_layer
    return seen

total = Counter()
for palm in palms:
    total += bfs_distances(cells, [palm])

min_distance = float('inf')
for pos in total:
    if pos not in palms:
        min_distance = min(min_distance, total[pos])
print(min_distance)

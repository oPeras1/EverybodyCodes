import itertools

stars = []
with open('../input.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '.' and lines[i][j] != '\n':
                stars.append((i + 1, j + 1)) 

def distance(star1, star2):
    return abs(star1[0] - star2[0]) + abs(star1[1] - star2[1])

edges = []
for (i, star1), (j, star2) in itertools.combinations(enumerate(stars), 2):
    edges.append((distance(star1, star2), i, j))

parent = list(range(len(stars)))

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    root1, root2 = find(v1), find(v2)
    if root1 != root2:
        parent[root2] = root1

edges.sort()
total_distance = 0
connections = []

for dist, i, j in edges:
    if find(i) != find(j):
        union(i, j)
        connections.append((i, j, dist))
        total_distance += dist

total_distance += len(stars)
print(total_distance)

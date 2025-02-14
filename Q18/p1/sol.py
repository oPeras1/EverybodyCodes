
p = 0

map = []
with open('../input.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '.' or lines[i][j] == 'P':
                map.append((i, j))
                if lines[i][j] == 'P':
                    p+=1

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

queue = [(1,0)]
visited = set()
visited.add((1,0))

time = -1

while queue:
    time += 1
    queue2 = []

    for i, j in queue:
        for d in dirs:
            y, x = i+d[0], j+d[1]

            if (y, x) in map and (y, x) not in visited:
                visited.add((y, x))
                queue2.append((y, x))

                if lines[y][x] == 'P':
                    p -= 1
                    if p == 0:
                        print(time+1)
                        exit()
    
    queue = queue2
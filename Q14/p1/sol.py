mov = []
with open("../input.txt") as f:
    line = f.readline().strip()
    mov = line.split(",")

base = 0
maxh = 0

for move in mov:
    if move[0] == 'U':
        base += int(move[1:])
    elif move[0] == 'D':
        base -= int(move[1:])
    maxh = max(maxh, base)

print(maxh)

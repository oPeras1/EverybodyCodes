from collections import defaultdict
from copy import deepcopy

loop = []

mapping = defaultdict(lambda: defaultdict(chr))

rotationpoins = []

with open('../input.txt') as f:
    lines = f.read().splitlines()

    loop = list(lines[0])

    for i in range(2, len(lines)):
        for j in range(len(lines[i])):
            mapping[i-2][j] = lines[i][j]

            if i == 3 and 0 < j < len(lines[i])-1:
                rotationpoins.append((i-2,j))

def rotate(mapp, pos, dir):

    copymappp = deepcopy(mapp)

    y = pos[0]
    x = pos[1]

    if dir == 'R':
        mapp[y-1][x-1] = copymappp[y][x-1]
        mapp[y-1][x] = copymappp[y-1][x-1]
        mapp[y-1][x+1] = copymappp[y-1][x]

        mapp[y][x+1] = copymappp[y-1][x+1]

        mapp[y+1][x+1] = copymappp[y][x+1]
        mapp[y+1][x] = copymappp[y+1][x+1]
        mapp[y+1][x-1] = copymappp[y+1][x]

        mapp[y][x-1] = copymappp[y+1][x-1]
    elif dir == 'L':
        mapp[y-1][x-1] = copymappp[y-1][x]
        mapp[y-1][x] = copymappp[y-1][x+1]
        mapp[y-1][x+1] = copymappp[y][x+1]

        mapp[y][x+1] = copymappp[y+1][x+1]

        mapp[y+1][x+1] = copymappp[y+1][x]
        mapp[y+1][x] = copymappp[y+1][x-1]
        mapp[y+1][x-1] = copymappp[y][x-1]

        mapp[y][x-1] = copymappp[y-1][x-1]

    return mapp

while mapping[1][0] != '>' or mapping[1][len(mapping[1])-1] != '<':

    count = -1
    for i in range(len(rotationpoins)):
        count += 1
        if count >= len(loop):
            count = 0

        mapping = rotate(mapping, rotationpoins[i], loop[count])

phrase = ""

for i in range(1, len(mapping[1])-1):
    phrase += mapping[1][i]

print(phrase)
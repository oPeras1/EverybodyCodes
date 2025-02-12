from collections import defaultdict

data = []

with open('../input.txt', 'r') as file:
    numberso = file.readline().strip().split(",")
    
    data = [[] for _ in range(len(numberso))]

    file.readline()

    for line in file:
        j = -1
        for i in range(0, len(line), 4):
            j += 1
            face = line[i:i+3]
            if (face.count(" ") == 0 and len(face) == 3):
                data[j].append(face)
                
def getcoin(caface):
    chars = set(caface.strip())

    coin = 0

    for c in chars:
        num = caface.count(c)
        if num == 3:
            coin += 1
        if num > 3:
            coin += num-2
    
    return coin


numbers = []

for i in range(len(numberso)):
    numberso[i] = int(numberso[i])
    numbers.append(0)


totalcoins = 0

coinshistory = defaultdict(int)

total = 202420242024

for j in range(0,total):
    catfaces = ""
    indexes = tuple()
    for i in range(len(numbers)):
        numbers[i] += numberso[i]
        numbers[i] = numbers[i] % len(data[i])

        catfaces = catfaces + data[i][numbers[i]][0]+data[i][numbers[i]][2]
        indexes += (numbers[i],)

    if indexes in coinshistory:
        l = j - coinshistory[indexes][0]

        div = total // l

        rest = total % l

        totalcoins *= div


        for h in coinshistory:
            if coinshistory[h][0] == rest-1:
                totalcoins += coinshistory[h][1]
                break

        break

    coin = getcoin(catfaces)

    totalcoins += coin    
    
    coinshistory[indexes] = (j, totalcoins)

print(totalcoins)




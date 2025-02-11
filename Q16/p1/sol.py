from collections import defaultdict

data = []

with open('../input.txt', 'r') as file:
    numbers = file.readline().strip().split(",")
    
    data = [[] for _ in range(len(numbers))]

    file.readline()

    for line in file:
        j = -1
        for i in range(0, len(line), 4):
            j += 1
            face = line[i:i+3]
            if (face != "   "):
                data[j].append(face)
                
catfaces = ""

for i in range(len(numbers)):
    n = int(numbers[i]) * 100
    n = n % len(data[i])

    catfaces = catfaces + data[i][n] + " "

print(catfaces)

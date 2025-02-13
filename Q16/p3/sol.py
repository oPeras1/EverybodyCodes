from collections import defaultdict

with open('../input.txt', 'r') as file:
    numberso = list(map(int, file.readline().strip().split(',')))
    data = [[] for _ in range(len(numberso))]

    file.readline()

    for line in file:
        line = line.rstrip('\n')
        j = -1
        for i in range(0, len(line), 4):
            j += 1
            face = line[i:i+3].strip()
            if len(face) == 3 and face.count(' ') == 0:
                data[j].append(face)

eyes = []
for wheel in data:
    wheel_eyes = []
    for face in wheel:
        left = face[0]
        right = face[2]
        wheel_eyes.append((left, right))
    eyes.append(wheel_eyes)

wheel_lengths = [len(wheel) for wheel in data]
steps = numberso

state_coins = {}
def coins_for_state(state):
    if state in state_coins:
        return state_coins[state]
    all_eyes = []

    for i, pos in enumerate(state):
        left, right = eyes[i][pos]
        all_eyes.append(left)
        all_eyes.append(right)
    counts = defaultdict(int)

    for c in all_eyes:
        counts[c] += 1
    total = 0

    for cnt in counts.values():
        if cnt >= 3:
            total += cnt - 2
    state_coins[state] = total
    return total

current_max = defaultdict(lambda: -float('inf'))
current_min = defaultdict(lambda: float('inf'))

initial_state = tuple([0] * len(data))

current_max[initial_state] = 0
current_min[initial_state] = 0

for _ in range(256):
    new_max = defaultdict(lambda: -float('inf'))
    new_min = defaultdict(lambda: float('inf'))
    
    for state in current_max:
        current_max_coin = current_max[state]
        current_min_coin = current_min[state]

        for delta in (-1, 0, 1):
            new_state = []
            for i in range(len(state)):

                adjusted = (state[i] + delta) % wheel_lengths[i]

                new_pos = (adjusted + steps[i]) % wheel_lengths[i]
                new_state.append(new_pos)
            new_state_tuple = tuple(new_state)
            coins = coins_for_state(new_state_tuple)


            new_max[new_state_tuple] = max(new_max[new_state_tuple], current_max_coin + coins)
            new_min[new_state_tuple] = min(new_min[new_state_tuple], current_min_coin + coins)

    current_max = new_max
    current_min = new_min

max_result = max(current_max.values())
min_result = min(current_min.values())
print(f"{max_result} {min_result}")
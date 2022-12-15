# 2019 BIO Q2


# a）
disappear, instructions, moves = input().split()
current = (0, 0)
turns = {"L": 3, "R": 1, "F": 0}
directions = {"1": [0, 1], "2": [1, 0], "3": [0, -1], "0": [-1, 0]}
trails = {}
direction = 1

for move in range(int(moves)):
    ins = move % len(instructions)
    direction = (direction + turns[instructions[ins]]) % 4
    valid_move = False
    for turn in range(4):
        if not valid_move:
            if (current[0] + directions[str(direction)][0], current[1] + directions[str(direction)][1]) in trails:
                direction = (direction + 1) % 4
            else:
                valid_move = True
                trails[current] = 0
                current = (current[0] + directions[str(direction)][0], current[1] + directions[str(direction)][1])
    if not valid_move:
        break
    for disappearing in trails:
        trails[disappearing] += 1
    temp = trails.copy()
    for item in trails:
        if trails[item] >= int(disappear):
            temp.pop(item)
    trails = temp.copy()
print(current)
# b)
print(trails)

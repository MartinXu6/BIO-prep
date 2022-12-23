#BIO 2020 Q2

plan, q, p = input().split()
rooms = len(plan) + 2
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
connections = {}
chosen = []
# first part, constructing the room plan
while len(plan) != 0:
    for i in alpha:
        if i not in plan and i != "|":
            chosen.append(i)
            alpha = alpha.replace(i, "|")
            connections[i] = connections.get(i, "") + plan[0]
            connections[plan[0]] = connections.get(plan[0], "") + i
            break
    plan = plan[1:]
first, second = [l for l in alpha[:rooms] if l != "|"]
connections[first] = connections.get(first, "") + second
connections[second] = connections.get(second, "") + first
chosen.append(first)
chosen.append(second)
for letter in sorted(connections):
    print("".join(sorted(connections[letter])))

# second part(the moving between the rooms)
room_visited = {}  # the dictionary containing the number of times each room has been visited
exit_used = {}  # the dictionary containing number of times the explorer has left through the exits of the room
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for x in alpha:
    room_visited[x] = room_visited.get(x, 0)
for o in alpha:
    exit_used[o] = exit_used.get(o, dict())
    if o in chosen:
        for s in sorted(connections[o]):
            exit_used[o][s] = exit_used[o].get(s, 0)
            # plug in the exits for each room, set the default visiting times to 0

current_room = "A"
output = ""
for y in range(int(p)):
    exits = sorted(connections[current_room])  # this is the exits of a room in alphabetical order
    room_visited[current_room] += 1
    if room_visited[current_room] % 2 != 0:  # if visited the room odd number of times
        exit_used[current_room][exits[0]] += 1  # leave through the first alphabetical exit
        current_room = exits[0]  # now he is in a new room
    else:  # if the room has been visited even number of times
        for exit_ in exit_used[current_room]:  # checking the exits in alphabetical order
            if exit_used[current_room][exit_] % 2 != 0:  # if the exit has been visited odd number of times
                if exit_ == exits[-1]:  # if the exit is the last alphabetically
                    exit_used[current_room][exit_] += 1  # leave through the last exit
                    current_room = exit_
                    break
                else:  # if the exit is not the last alphabetically
                    exit_used[current_room][exits[exits.index(exit_) + 1]] += 1  # the explorer leaves through the next
                    # alphabetically exit
                    current_room = exits[exits.index(exit_) + 1]
                    break
    if y == int(q) - 1:  # after q+1 rounds of exploring, record the current room as it starts at 0
        output += current_room
print(output + current_room)

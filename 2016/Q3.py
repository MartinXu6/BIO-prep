def is_prime(n):
    if n == 2:
        return True
    elif n <= 1:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True


def connected(n, top):
    con_lst = []
    power = 0
    while True:
        if is_prime(n - 2 ** power) and n - 2 ** power > 1:
            con_lst.append(n - 2 ** power)
            power += 1
        elif n - (2 ** power) < 1:
            break
        else:
            power += 1
    power = 0
    while True:
        if is_prime(n + 2 ** power) and n + 2 ** power <= top:
            con_lst.append(n + 2 ** power)
            power += 1
        elif n + (2 ** power) > top:
            break
        else:
            power += 1
    return con_lst


def BFS(p, q, top):
    visited = [p]
    current = connected(p,top)
    layer = 1
    next = []
    while current:
        layer += 1
        for node in current:
            if node not in visited:
                visited.append(node)
                if node == q:
                    return layer
            next += connected(node,top)
        current = set(next)
        next = []


highest, start, end = map(int, input().split())
print(BFS(start, end, highest))


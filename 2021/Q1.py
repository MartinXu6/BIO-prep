# 2021 BIO Q1

a, b = input().split()


def pat(string):
    ord_list = [ord(x) for x in string]
    if len(string) == 1:
        return True
    for i in range(len(string) - 1):
        if min(ord_list[:i + 1]) > max(ord_list[i + 1:]):
            if pat(string[:i + 1][::-1]) and pat(string[i + 1:][::-1]):
                return True
    else:
        return False


for test in a, b, a + b:
    print("YES") if pat(test) else print("NO")

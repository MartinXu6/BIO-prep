encrypted = input()
value_list = [ord(i)-64 for i in encrypted]
for i in range(len(value_list)):
    if value_list[i] > sum(value_list[:i]):
        value_list[i] -= sum(value_list[:i])
    else:
        value_list[i] -= (sum(value_list[:i]))%26
        if value_list[i] < 1:
            value_list[i] += 26
print("".join([chr(l+64) for l in value_list]))

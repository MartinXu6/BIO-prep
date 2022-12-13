# 2017 BIO Q1


first_line = input()
current_line = first_line[:]
RGB = "RGB"
for line in range(len(first_line) - 1):
    temp = ""
    for l in range(len(current_line) - 1):
        if current_line[l] == current_line[l + 1]:
            temp += current_line[l]
        else:
            for x in RGB:
                if x != current_line[l] and x != current_line[l + 1]:
                    temp += x
    current_line = temp
print(current_line)

# 2020 BIO Q1


string, steps = input().split()
values = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5,
          "IV": 4,
          "I": 1}

for step in range(int(steps)):
    index = 0
    temp = []
    for letter in range(len(string)):
        if letter == index:
            length = 0
            for l in range(letter, len(string)):
                if l == len(string) - 1:
                    index = l + 1
                if string[l] == string[letter]:
                    length += 1
                else:
                    index = l
                    break
            while length != 0:
                for i in values:
                    if length >= values[i]:
                        length -= values[i]
                        temp.append(i)
            temp.append(string[letter])
    string = list("".join(temp))
string = "".join(string)
print(f"{string.count('I')} {string.count('V')}")

# 2019 BIO Q1

number = input()
palindrome = list(number)
last = 0


def generation(string):
    string = string[:len(string) // 2 + len(string) % 2] + string[:len(string) // 2][::-1]
    return string


# very ugly code below

while int("".join(list(palindrome))) <= int(number) or palindrome != palindrome[::-1]:
    palindrome = generation(palindrome)
    if palindrome.count("9") == len(palindrome):
        palindrome = list(str(int("".join(palindrome)) + 2))
        break
    if palindrome == palindrome[::-1] and int("".join(list(palindrome))) > int(number):
        break
    else:
        if palindrome[len(palindrome) // 2 + len(palindrome) % 2 - 1 - last] == "9" and (
                len(palindrome) // 2 + len(palindrome) % 2 - 1 - last) == 0:
            palindrome = list(str(int("".join(palindrome)) + 1))
            continue
        elif palindrome[len(palindrome) // 2 + len(palindrome) % 2 - 1 - last] != "9":
            palindrome[len(palindrome) // 2 + len(palindrome) % 2 - 1 - last] = str(int(palindrome[len(palindrome) // 2 + len(palindrome) % 2 - 1 - last]) + 1)
        elif palindrome[len(palindrome) // 2 + len(palindrome) % 2 - 1 - last] == "9":
            palindrome[len(palindrome) // 2 + len(palindrome) % 2 - 1 - last] = "0"
            last += 1

print("".join(palindrome))

wording = input()


def frac(word):
    if word == "":
        return [1, 0, 0, 1]
    elif "R" not in word:
        left = frac(word[:-1])
        return [left[0], 0, left[2] + 1, 1]
    elif "L" not in word:
        right = frac(word[:-1])
        return [1, right[1] + 1, 0, right[3]]
    else:
        left = frac(word[:len(word) - word[::-1].index("L") - 1])
        right = frac(word[:len(word) - word[::-1].index("R") - 1])
        return [left[0] + right[0], left[1] + right[1], left[2] + right[2], left[3] + right[3]]


ans = frac(wording)
print(ans[0] + ans[1],"/", ans[2] + ans[3])

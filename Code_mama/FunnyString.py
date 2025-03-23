def is_funny(s):
    for i in range(len(s)):
        if (i % 2 == 0 and not s[i].islower()) or (i % 2 == 1 and not s[i].isupper()):
            return False
    return True

s = input().strip()

print("Yes" if is_funny(s) else "No")

s = input()

count = 0
if len(s) == 7 and s[0] == '#':
    for ch in s[1:]:
        if ch.isdigit() or ch in 'ABCDEF':
            count += 1

if count == 6:
    print("true")
else:
    print("false")

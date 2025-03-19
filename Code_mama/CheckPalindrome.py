def is_palindrome():
    string = input().strip()
    length = len(string)
    mid = length // 2
    count = 0

    for i in range(mid):
        if string[i] == string[length - 1 - i]:
            count += 1

    if count == mid:
        print("YES")
    else:
        print("NO")

is_palindrome()

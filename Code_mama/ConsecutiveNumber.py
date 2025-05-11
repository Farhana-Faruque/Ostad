def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()

    count = 0

    for i in range(n - 1):
        if arr[i] != arr[i + 1] and arr[i] + 1 == arr[i + 1]:
            count += 1

    if count == n - 1:
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()

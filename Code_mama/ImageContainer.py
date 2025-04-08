def main():
    weight = int(input())

    if 0 < weight < 1000:
        remain = 1000 - weight
        left = remain // 2
        print(left)
    else:
        print(0)

if __name__ == "__main__":
    main()

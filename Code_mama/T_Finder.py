def main():
    str_list = []
    count = 0
    
    for _ in range(10):
        s = input().strip()
        str_list.append(s)
        if 'T' in s:
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()

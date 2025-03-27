def main():
    start, end = map(int, input().split())
    
    if start >= end:
        diff = abs(start - 24)
        result = diff + end
    else:
        result = end - start
    
    print(result)

if __name__ == "__main__":
    main()

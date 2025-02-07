def division():
    a, b = map(int, input().split())
    if b == 0:
        return None
    c = a // b  
    return c

def main():
    div = division()
    if div is not None:
        print(div)

if __name__ == "__main__":
    main()


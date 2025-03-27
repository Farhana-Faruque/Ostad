def main():
    id, items = map(int, input().split())
    
    if id == 101:
        print(items * 10)
    elif id == 202:
        print(items * 25)
    elif id == 303:
        print(items * 5)
    
if __name__ == "__main__":
    main()

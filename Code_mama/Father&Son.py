def main():
    fAge, sAge = map(int, input().split())
    
    dou = sAge * 2
    diff = abs(fAge - dou)
    
    print(diff)

if __name__ == "__main__":
    main()

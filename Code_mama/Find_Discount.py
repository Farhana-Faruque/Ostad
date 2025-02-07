def discount():
    a, b = map(float, input().split())
    price = a - (a * (b / 100))
    return price

def main():
    price = discount()
    print(f"Price: {price:.2f}")

if __name__ == "__main__":
    main()
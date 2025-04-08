import math

def main():
    weight, height, radius = map(int, input().split())

    diagonal = math.sqrt(weight ** 2 + height ** 2)
    diameter = radius * 2

    if diagonal <= diameter:
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()

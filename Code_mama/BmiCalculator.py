def calculate_bmi(height, weight):
    bmi = weight / (height * height)
    return bmi

def main():
    height, weight = map(float, input().split())

    bmi = calculate_bmi(height, weight)
    print(f"BMI: {bmi:.2f}")

    if bmi < 18.5:
        print("Underweight")
    elif bmi >= 18.5 and bmi < 25:
        print("Normal weight")
    elif bmi >= 25 and bmi < 30:
        print("Overweight")
    else:
        print("Obese")

if __name__ == "__main__":
    main()

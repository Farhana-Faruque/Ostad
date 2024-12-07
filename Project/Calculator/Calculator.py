print("Welcome to the Calculator")
print("Which operation do you want to do??")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = int(input("Select the operation you want to do: "))

if option == 1:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = n1 + n2
    print("Addition is: " + str(n3))
elif option == 2:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = n1 - n2
    print("Subtraction is: " + str(n3))
elif option == 3:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = n1 * n2
    print("Multiplication is: " + str(n3))
elif option == 4:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = n1 / n2
    print("Division is: " + str(n3))
else: 
    print("Invalid input")

print("Thank you")

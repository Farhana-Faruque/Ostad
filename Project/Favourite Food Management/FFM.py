favourite_food = [] # Initialize an empty list for storing foods 

while True:
    print("Favourite Food Manager")
    print("0. Exit")
    print("1. Add foods")
    print("2. Remove foods")
    print("3. View all favourite foods")

    choice = input("Enter your choice: ") # User will give an input 
    
    if choice == '0':
        print("Thanks for using Favourite Food Manager")
        break
    elif choice == '1':
        food = input("Enter your favourite food: ")
        favourite_food.append(food)
        print(f"{food} has been added.")
    elif choice == '2':
        food = input("Enter a food name which you want to remove: ")
        favourite_food.remove(food)
        print(f"{food} has been removed.")
    elif choice == '3':
        if favourite_food:
            print("Your favourite foods are: ")
            for index , food in enumerate(favourite_food, start = 1):
                print(f"{index}.{food}")
        else:
            print("You didn't add any foods.")
    else: 
        print("Invalid choice.")

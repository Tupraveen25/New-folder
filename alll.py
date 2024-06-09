num1 = int(input('Enter 1st value: '))
num2 = int(input('Enter 2nd value: '))
choice = input("Enter choice (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division): ")

if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input. Please enter a number between 1 and 4.")

input("Press enter key to exit")

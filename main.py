# Interactive calculator

def menu():
    print("Select the operation:")
    print("1. Sum")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

def getNumber(value):
    while True:
        try:
            return float(input(value))
        except ValueError:
            print("Error: you must enter a valid number!")

def calculator():
    while True:
        menu()
        choice = input("Enter the operation number or 'q' to exit\n")

        if choice.lower() == 'q':
            print("Thanks for using calculator!")
            break
        else:
            if choice in ['1','2','3','4']:
                num1 = getNumber("Insert first number: ")
                num2 = getNumber("Insert second number: ")

                if choice == '1':
                    print(f"The sum is: {num1 + num2}")
                elif choice == '2':
                    print(f"The subtraction is: {num1 - num2}")
                elif choice == '3':
                    print(f"The multiplication is: {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"The division is: {num1 / num2}")
                    else:
                        print("Division by zero, error!")
            else:
                print("Invalid choice, try again!")

# Starting the program
calculator()
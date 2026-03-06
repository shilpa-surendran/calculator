from operations import add, subtract, divide

if __name__ == "__main__":
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")

    while True:
        choice = input("Enter choice(1/2/3): ")

        if choice in ('1', '2', '3'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                try:
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                except ValueError as e:
                    print(e)
            
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

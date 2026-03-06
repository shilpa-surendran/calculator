from operations import add, subtract

if __name__ == "__main__":
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")

    while True:
        choice = input("Enter choice(1/2): ")

        if choice in ('1', '2'):
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
            
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

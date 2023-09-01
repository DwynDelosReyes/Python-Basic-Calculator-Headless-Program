"""
Headless Basic Python Calculator
First Attempt
Author: Dwyn Delos Reyes
"""

# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Choose a number (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == "3":
            print(num1, "x", num2, "=", multiply(num1, num2))
        elif choice == "4":
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(num1, "/", num2, "=", result)

        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation == "no":
            break
    else:
        print("Invalid input. Please choose a valid operation.")

"""
Headless Basic Python Calculator 
First Attempt
Author: Dwyn Delos Reyes
"""

def add(x, y):
    
    return x + y

def subtract(x, y):
   
    return x - y

def multiply(x, y):
    
    return x * y

def divide(x, y):
    
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_number(prompt):
    
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_operation():
    
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    while True:
        operation = input("Enter operation (+, -, *, /): ")
        if operation in operations:
            return operations[operation]
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")

def calculator():
   
    print("Welcome to the Simple Command-Line Calculator!")

    while True:
        num1 = get_number("Enter first number: ")
        operation = get_operation()
        num2 = get_number("Enter second number: ")

        result = operation(num1, num2)
        print(f"Result: {result}")

        cont = input("Do you want to perform another calculation? (yes/no): ").lower()
        if cont != 'yes':
            break

    print("Thank you for using the calculator. Goodbye!")

if __name__ == "__main__":
    calculator()

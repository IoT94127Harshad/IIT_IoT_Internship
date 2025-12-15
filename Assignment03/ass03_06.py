#   6. Write different functions to perform basic arithmetic operations. Write another function with name
#      calculate which takes three arguments as operand1, operand2 and function to perfrom operation and
#      returns the result of operation. Test above function for different set of inputs


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b


def calculate(operand1, operand2, operation):
    return operation(operand1, operand2)

print("ENter values to Calculate:")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition:", calculate(x, y, add))
print("Subtraction:", calculate(x, y, subtract))
print("Multiplication:", calculate(x, y, multiply))
print("Division:", calculate(x, y, divide))

print("\nTesting with different values:")
print("Values are: 10 & 5")
print("Addition:", calculate(10, 5, add))
print("Subtraction:", calculate(10, 5, subtract))
print("Multiplication:", calculate(10, 5, multiply))
print("Division:", calculate(10,5,divide))

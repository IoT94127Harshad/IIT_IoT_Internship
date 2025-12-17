#    2. Create a module named calculator.py that contains the following functions:
#               add(a, b)
#               subtract(a, b)
#               multiply(a, b)
#               divide(a, b)
#       Write another Python program that imports this module and performs all operations for two user-input
#       numbers.

import calculator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", calculator.add(a, b))
print("Subtraction:", calculator.subtract(a, b))
print("Multiplication:", calculator.multiply(a, b))
print("Division:", calculator.divide(a, b))

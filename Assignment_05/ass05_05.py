#   5. Create a package named operations with the following structure:
#      operations/
#                   │── __init__.py
#                   │── arithmetic.py
#                   │── string_ops.py
#      arithmetic.py should contain functions for addition and multiplication.
#      string_ops.py should contain functions to reverse a string and count vowels.
#      Write a Python program to import this package and demonstrate all functions.


from arithmetic import add, multiply
from string_ops import reverse_string, count_vowels

print(" Arithmetic Operations")
print("Addition:", add(10, 5))
print("Multiplication:", multiply(10, 5))

print("\n String Operations")
text = input("Enter a string: ")

print("Reversed String:", reverse_string(text))
print("Number of Vowels:", count_vowels(text))




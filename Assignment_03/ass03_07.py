# 7. Write recursive function to find factorial and power.


def factorial(n):
    if n == 0 or n == 1:   
        return 1
    else:
        return n * factorial(n - 1)


def power(base, exp):
    if exp == 0:      
        return 1
    else:
        return base * power(base, exp - 1)



num = int(input("Enter number: "))
print("Factorial of", num, "=", factorial(num))

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print(base, "power", exponent, "=", power(base, exponent))
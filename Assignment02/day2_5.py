#    5. Write a function to print a given number in binary format.

def print_binary(n):
    print(bin(n)[2:])

num = int(input("Enter a number: "))
print_binary(num)

def print_binary(n):
    if n == 0:
        print(0)
        return

    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

    print(binary)

num = int(input("Enter a number: "))
print_binary(num)

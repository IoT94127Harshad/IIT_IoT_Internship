#   4. Write a function to check number is prime or not and print prime numbers in the given range.


def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers in the given range are:")
for num in range(start, end + 1):
        if prime(num):
            print(num, end=" ")

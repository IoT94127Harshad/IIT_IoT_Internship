#    2. Write a program to accept 5 digit number and check whether it is a numeric palindrome. (if reversed
#       number is same as entered number it is called as palindrome)


num = int(input("Enter 5 digit number: "))

temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if num == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

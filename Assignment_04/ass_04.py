#   4. Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For
#      example, histogram([4, 9, 7]) should print the following:
#       4: ****
#       9: *********
#       7: *******
 
 
def histogram (a ,b ,c):
    for num in a ,b ,c:
        print("*" *num)
        
   
        
        
a = int(input("Enter 1st number: "))
b = int(input("Enter 2st number: "))
c = int(input("Enter 3st number: "))
histogram(a, b, c)
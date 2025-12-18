#    3. Define a function overlapping() that takes two lists and returns True if they have at least one member in
#       common, False otherwise.
 
 
def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = input("Enter elements of first list separated by space: ").split()
list2 = input("Enter elements of second list separated by space: ").split()

print(overlapping(list1, list2))

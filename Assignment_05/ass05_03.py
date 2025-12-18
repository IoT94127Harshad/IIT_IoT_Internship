#    3. Create a module named geometry.py with functions to calculate:
#           Area of a circle
#           Area of a rectangle
#       Write a Python program that imports only the required functions from the module and calculates areas
#       based on user input.


from geometry import area_circle, area_rectangle


r = float(input("Enter radius of the circle: "))
circle_area = area_circle(r)
print("Area of Circle:", circle_area)

l = float(input("\nEnter length of rectangle: "))
w = float(input("Enter width of rectangle: "))
rect_area = area_rectangle(l, w)
print("Area of Rectangle:", rect_area)

#   2. Write a lambda functions to convert kilometers to meters, meters to centimeters, centimeters to
#       millimeters, feets to inches, and inches to centimeter. Write a function distance_converter() that takes a
#       distance, conversion type as a string (e.g. km to m, m to cm, etc.) and a conversion function as
#       argument. This function does the converion using given function and print the result. Input a distance
#       from user and print all conversions.




km_to_m = lambda n : n* 1000
m_to_cm = lambda n : n* 100
cm_to_mm = lambda n : n* 10
feet_to_inches = lambda n : n* 12
inches_to_cm = lambda n : n* 2.54



def distance_converter(distance, conversion_type):
    
    print(f"{conversion_type}: ")

value = float(input("Enter a distance value: "))

print("\nConverted Values:")

distance_converter(value, f"Kilometers to Meters (km → m) {km_to_m(value)}")
distance_converter(value, f"Meters to Centimeters (m → cm) {m_to_cm(value)}")
distance_converter(value, f"Centimeters to Millimeters (cm → mm) {cm_to_mm(value)}")
distance_converter(value, f"Feet to Inches (ft → in) {feet_to_inches(value)}")
distance_converter(value, f"Inches to Centimeters (in → cm){inches_to_cm(value)}")
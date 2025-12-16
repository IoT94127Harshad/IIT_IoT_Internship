#   1. Write functions to convert kilometers to meters, meters to centimeters, centimeters to millimeters, feets
#      to inches, and inches to centimeter. Write a function distance_converter() that takes a distance,
#      conversion type as a string (e.g. km to m, m to cm, etc.) and a conversion function as argument. This
#      function does the converion using given function and print the result. Input a distance from user and
#      print all conversions.




def km_to_m(km):
    return km * 1000

def m_to_cm(m):
    return m * 100

def cm_to_mm(cm):
    return cm * 10

def feet_to_inches(ft):
    return ft * 12

def inches_to_cm(inch):
    return inch * 2.54

def distance_converter(distance, conversion_type, conversion_func):
    result = conversion_func(distance)
    print(f"{conversion_type}: {result}")

value = float(input("Enter a distance value: "))

print("\nConverted Values:")

distance_converter(value, "Kilometers to Meters (km → m)", km_to_m)
distance_converter(value, "Meters to Centimeters (m → cm)", m_to_cm)
distance_converter(value, "Centimeters to Millimeters (cm → mm)", cm_to_mm)
distance_converter(value, "Feet to Inches (ft → in)", feet_to_inches)
distance_converter(value, "Inches to Centimeters (in → cm)",inches_to_cm)
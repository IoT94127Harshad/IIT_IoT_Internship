#   5. Create a list of lambda functions that converts from tonns to kilograms, kilograms to grams, grams to
#      milligrams, and milligrams to pounds. Input a weight from user in tonns and print it in remaining all
#      units. E.g. if user inputs 0.002 tonns, then output should be 2 kg, 2000gm, 2000000 mg, and
#      4.409245244 lbs.

 
 
conversions = [
    lambda t: t * 1000,                 
    lambda kg: kg * 1000,                
    lambda g: g * 1000,                
    lambda mg: mg * 0.00000220462        
]

tonnes = float(input("Enter weight in tonnes: "))

kg = conversions[0](tonnes)
gm = conversions[1](kg)
mg = conversions[2](gm)
lbs = conversions[3](mg)

print(f"{kg} kg")
print(f"{gm} gm")
print(f"{mg} mg")
print(f"{lbs} lbs")

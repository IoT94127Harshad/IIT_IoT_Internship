#   1. Explore python math and os module. [upload your codes on git]



#import math

#num = 25
#angle = 45

#print(f"__name__ = {math.__name__}")
#print("Square root of", num, ":", math.sqrt(num))
#print("Factorial of 5 :", math.factorial(5))
#print("Power (2^3) :", math.pow(2, 3))
#print("Ceil of 4.3 :", math.ceil(4.3))
#print("Floor of 4.7 :", math.floor(4.7))
#print("Absolute value of -10 :", math.fabs(-10))
#print("Sin 45° :", math.sin(math.radians(angle)))
#print("Cos 45° :", math.cos(math.radians(angle)))
#print("Pi value :", math.pi)
#print("e value :", math.e)




import math as m

num = 25
angle = 45

print(f"__name__ = {m.__name__}")
print("Square root of", num, ":", m.sqrt(num))
print("Factorial of 5 :", m.factorial(5))
print("Power (2^3) :", m.pow(2, 3))
print("Ceil of 4.3 :", m.ceil(4.3))
print("Floor of 4.7 :", m.floor(4.7))
print("Absolute value of -10 :", m.fabs(-10))
print("Sin 45° :", m.sin(m.radians(angle)))
print("Cos 45° :", m.cos(m.radians(angle)))
print("Pi value :", m.pi)
print("e value :", m.e)
    

import os
print("Current Working Directory:", os.getcwd())
print("List of files in current directory:")
print(os.listdir())

dir_name = "demo_folder"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print("Directory created:", dir_name)
else:
    print("Directory already exists:", dir_name)

file_path = os.path.join(dir_name, "sample.txt")
with open(file_path, "w") as f:
    f.write("This file is created using os module.")

print("File created at:", file_path)

new_file_path = os.path.join(dir_name, "renamed_sample.txt")
os.rename(file_path, new_file_path)
print("File renamed to:", new_file_path)

os.remove(new_file_path)
print("File deleted")

os.rmdir(dir_name)
print("Directory deleted")

print("\n Program execution completed successfully.")






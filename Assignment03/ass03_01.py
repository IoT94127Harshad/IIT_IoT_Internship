# 1. Explore built-in methods that you can use on strings. [upload all your demos on git]


text = "  Python Programming  "

print("Original:", text)
print("Lower:", text.lower())
print("Upper:", text.upper())
print("Strip:", text.strip())
print("Replace:", text.replace("Python", "Java"))
print("Find:", text.find("Program"))
print("Count of 'm':", text.count("m"))
print("Starts with Python:", text.strip().startswith("Python"))
print("Ends with ing:", text.strip().endswith("ing"))
print("Lowercase + uppercase:",text.swapcase())
print("Adding symbols in between:","-".join(["Python","Programming"]))
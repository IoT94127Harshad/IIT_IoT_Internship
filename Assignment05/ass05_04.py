#   4. Write a Python program that:
#       Imports the datetime module
#       Displays the current date and time
#       Prints the day of the week for the current date


import datetime

current_datetime = datetime.datetime.now()

print("Current Date and Time:", current_datetime)

day_name = current_datetime.strftime("%A")
print("Day of the Week:", day_name)

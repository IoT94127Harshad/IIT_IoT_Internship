#   8. Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
#      Input: ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
#      Output: [30.5, 34.25, 27.0, 23.25]


data = ((10, 10, 10, 12),
        (30, 45, 56, 45),
        (81, 80, 39, 32),
        (1, 2, 3, 4))

averages = []
for col in zip(*data):
    avg = sum(col) / len(col)
    averages.append(avg)

print(averages)

#    7. Create matrix of dim 3x4 as list of list with few fixed values. Create another matrix of dim 3x4 as tuple of
#       tuple with few fixed values. Create a function that takes these two matrices as params and calculate
#       their addition & subtraction. The function should return both result matrices and they should be
#       printed in main.




matrix_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matrix_tuple = (
    (12, 11, 10, 9),
    (8, 7, 6, 5),
    (4, 3, 2, 1)
)

def add_sub_matrices(m1, m2):
    addition = []
    subtraction = []

    for i in range(3):
        add_row = []
        sub_row = []
        for j in range(4):
            add_row.append(m1[i][j] + m2[i][j])
            sub_row.append(m1[i][j] - m2[i][j])
        addition.append(add_row)
        subtraction.append(sub_row)

    return addition, subtraction


add_result, sub_result = add_sub_matrices(matrix_list, matrix_tuple)

print("Addition Result:")
for row in add_result:
    print(row)

print("\nSubtraction Result:")
for row in sub_result:
    print(row)

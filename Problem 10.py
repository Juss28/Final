import numpy as np

# Given input matrix
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Convert the input matrix to a NumPy array
np_matrix = np.array(input_matrix)

# Calculate the sum of rows
row_sums = np.sum(np_matrix, axis=1)

# Calculate the sum of columns
col_sums = np.sum(np_matrix, axis=0)

print("Sum of rows:", row_sums)
print("Sum of columns:", col_sums)
# Define the matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Initialize sum
diagonal_sum = 0

# Iterate over the diagonal elements and add them up
for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]

# Print the sum
print("Sum of diagonal elements:", diagonal_sum)
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed_matrix = [[0]*rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

# Given input matrix
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose the matrix
output_matrix = transpose_matrix(input_matrix)

# Print the transposed matrix
for row in output_matrix:
    print(row)
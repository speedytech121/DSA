# transpose the matrix
# then reverse each rows to get the result


def rotate_ninty_degree(matrix):
    n  = len(matrix)
    print("orignal matrix")
    for row in matrix:
        print(row)
    
    # step 1: transpone the matrix(swap rows and columns)
    for i in range(n):
        for j in range(i+1, n): # swap only upper triangle elements
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    print("\n after transposing")
    for row in matrix:
        print(row)

    for i in range(n):
        matrix[i].reverse()
    
    print("\n after reversing each row")
    for row in matrix:
        print(row)



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate_ninty_degree(matrix)

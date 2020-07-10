def rotate(matrix):
    #return [[row[i] for row in matrix][::-1] for i in range(len(matrix))]
    N = len(matrix)
    matrix.reverse()
    for r in range(N):
        for c in range(r):
            matrix[r][c] , matrix[c][r]= matrix[c][r], matrix[r][c]  

    return matrix


matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

print(rotate(matrix))
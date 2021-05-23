n = int(input())
matrix = [[0 for i in range(n)] for j in range(n)]
number = 1
m = 1
matrix[n // 2][n // 2] = n * n
for i in range(n // 2):
    for j in range(n - m):
        matrix[i][j + i] = number
        number += 1
    for j in range(i, n - m + i):
        matrix[j][n - i - 1] = number
        number += 1
    for j in range(n - i - 1, i, -1):
        matrix[n - i - 1][j] = number
        number += 1
    for j in range(i, n - m + i):
        matrix[n - j - 1][i] = number
        number += 1

    m += 2
for line in matrix:
    print(*line, sep='\t')

import sys

A = [2, 4, 1, 3, 2, 4, 6, 7, 9, 2, 19]
B = [2, 1, 4, 3, 6, 9]

A.sort(key=lambda x: B.index(x) - sys.maxsize if x in B else - len(B) - x)
print(A)

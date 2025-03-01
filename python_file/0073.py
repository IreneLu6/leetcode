from typing import List


def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m,n=len(matrix),len(matrix[0])
    row,col=[false]*m,[false]*n

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == false:
                row[i]=col[j]=true

    for i in range(m):
        for j in range(n):
            if row[i] or col[j]:
                matrix[i][j]=0



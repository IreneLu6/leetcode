from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    matrix.reverse()
    m,n=len(matrix),len(matrix[0])
    for i in range(m):
        for j in range(i,n):
            tmp=matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=tmp


matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
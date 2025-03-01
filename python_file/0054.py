from typing import List


def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    S_O=[]
    m,n=len(matrix),len(matrix[0])
    left,right,top,bottom=0,n-1,0,m-1
    while left<=right and top<=bottom:
        for i in range(left,right+1):
            S_O.append(matrix[top][i])
        top+=1
        for i in range(top,bottom+1):
            S_O.append(matrix[i][right])
        right-=1
        if top <= bottom:
            for i in range(right,left-1,-1):
                S_O.append(matrix[bottom][i])
        bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                S_O.append(matrix[i][left])
        left+=1
    return S_O
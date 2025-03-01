
def numIslands(self, grid: List[List[str]]) -> int:
    def dfs(grid:List[List[str]],r,c):
        nr=len(grid)
        nc=len(grid[0])
        grid[r][c]='0'

        if r-1>=0 and grid[r-1][c] == '1':
            dfs(grid,r-1,c)
        if r+1<=nr-1 and grid[r+1][c] == '1':
            dfs(grid,r+1,c)
        if c-1>=0 and grid[r][c-1] == '1':
            dfs(grid,r,c-1)
        if c+1<=nc-1 and grid[r][c+1] == '1':
            dfs(grid,r,c+1)


    nr = len(grid)
    if nr==0:
        return 0
    nc = len(grid[0])
    numIsland=0

    for i in range(nr):
        for j in range(nc):
            if grid[i][j]=='1':
                numIsland+=1
                dfs(grid,i,j)
    return numIsland

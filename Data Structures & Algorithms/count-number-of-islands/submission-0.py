class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        def dfs(row, col):
            if row < 0 or row > rows-1 or col < 0 or col > columns - 1 or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            dfs(row + 1,col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        num_island = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    num_island += 1
                    dfs(i,j)
        return num_island
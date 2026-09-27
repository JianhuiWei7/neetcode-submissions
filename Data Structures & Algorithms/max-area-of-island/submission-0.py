class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        def dfs(row, col):
            if row < 0 or row > rows-1 or col < 0 or col > columns - 1 or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            area = 1
            area += dfs(row + 1,col)
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row, col - 1)
            return area
        num_island = 0
        max_area = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    total_area = dfs(i,j)
                    max_area = max(max_area, total_area)
        return max_area
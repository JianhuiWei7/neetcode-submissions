class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    queue.append([i,j])
        current_level = 0
        while queue:
            current_level += 1
            num_current_level = len(queue)
            count = 0
            while count < num_current_level:
                count += 1
                item = queue.popleft()
                for direction in [(1,0), (-1,0), (0,1), (0,-1)]:
                    x = item[0] + direction[0]
                    y = item[1] + direction[1]
                    if x < 0 or x > rows - 1 or y < 0 or y > columns -1:
                        continue
                    if grid[x][y] == 2147483647:
                        grid[x][y] = current_level
                        queue.append([x,y])
        

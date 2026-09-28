class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        queue = []
        fresh = 0
        minute = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
        def make_rotten(i,j):
            if i < 0 or i > rows - 1 or j < 0 or j > columns - 1:
                return None
            if grid[i][j] == 1:
                grid[i][j] = 2
                return [i,j]
            if grid[i][j] == 0 or grid[i][j] == 2:
                return None
        while queue:
            current_level = len(queue)
            count = 0
            if fresh > 0:
                minute += 1
            else:
                break
            while count < current_level:
                count += 1
                rotten = queue.pop(0)
                next_rot = make_rotten(rotten[0] + 1, rotten[1])
                if next_rot:
                    fresh -= 1
                    queue.append(next_rot)
                next_rot = make_rotten(rotten[0] - 1, rotten[1])
                if next_rot:
                    fresh -= 1
                    queue.append(next_rot)
                next_rot = make_rotten(rotten[0], rotten[1] + 1)
                if next_rot:
                    fresh -= 1
                    queue.append(next_rot)
                next_rot = make_rotten(rotten[0], rotten[1] - 1)
                if next_rot:
                    fresh -= 1
                    queue.append(next_rot)
        if fresh > 0:
            return -1
        else:
            return minute



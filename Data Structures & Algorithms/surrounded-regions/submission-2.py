class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        columns = len(board[0])
        up_borader = [[0, col] for col in range(columns - 1)] 

        right_borader = [[row, columns-1] for row in range(rows - 1)]

        down_borader = [[rows-1, col] for col in range(1, columns)]

        left_borader = [[row, 0] for row in range(1, rows)]

        borader = up_borader + right_borader + down_borader + left_borader
        queue = deque()
        free = [[0 for _ in range(columns)] for _ in range(rows)]
        for row, col in borader:
            if board[row][col] == "O":
                queue.append([row,col])
                free[row][col] = 1
        while queue:
            item = queue.popleft()
            for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
                row = item[0] + direction[0]
                col = item[1] + direction[1]
                if row < 0 or row > rows - 1 or col < 0 or col > columns - 1:
                    continue
                if free[row][col] == 1:
                    continue
                if board[row][col] == "O":
                    queue.append([row,col])
                    free[row][col] = 1
        for row in range(rows):
            for col in range(columns):
                if board[row][col] == "O" and free[row][col] == 0:
                    board[row][col] = "X"
        





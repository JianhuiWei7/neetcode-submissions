class Solution:
    def solveNQueens(self, n: int):
        available = [[1] * n for _ in range(n)]
        path = []  # 每一行的皇后所在列
        result = []

        def dfs(row):
            if row == n:
                result.append([
                    "." * col + "Q" + "." * (n - col - 1)
                    for col in path
                ])
                return

            for col in range(n):
                if available[row][col] == 0:
                    continue

                path.append(col)
                changed = []

                # 标记下方同列和两条对角线
                for r in range(row + 1, n):
                    distance = r - row

                    for c in (col, col - distance, col + distance):
                        if 0 <= c < n and available[r][c] == 1:
                            available[r][c] = 0
                            changed.append((r, c))

                dfs(row + 1)

                # 只恢复本次修改的位置
                for r, c in changed:
                    available[r][c] = 1

                path.pop()

        dfs(0)
        return result
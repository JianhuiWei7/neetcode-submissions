from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, index):
            # 已匹配完整个单词
            if index == len(word):
                return True

            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
                or (r, c) in visited
                or board[r][c] != word[index]
            ):
                return False

            visited.add((r, c))

            found = (
                dfs(r + 1, c, index + 1)
                or dfs(r - 1, c, index + 1)
                or dfs(r, c + 1, index + 1)
                or dfs(r, c - 1, index + 1)
            )

            visited.remove((r, c))  # 回溯：撤销当前格子的使用标记
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
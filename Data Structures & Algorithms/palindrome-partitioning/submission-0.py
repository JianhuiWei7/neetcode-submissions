from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def dfs(start):
            # 整个字符串都已经切分完
            if start == len(s):
                result.append(path.copy())
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                # 不是回文，跳过这种切法
                if substring != substring[::-1]:
                    continue

                path.append(substring)
                dfs(end)
                path.pop()  # 撤销选择，尝试其他切法

        dfs(0)
        return result
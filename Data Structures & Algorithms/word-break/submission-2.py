from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def match(string, word):
            return string[:len(word)] == word

        found = 0
        failed = set()

        def dfs(string):
            nonlocal found

            if found or string in failed:
                return

            if len(string) == 0:
                found = 1
                return

            for word in wordDict:
                if match(string, word):
                    dfs(string[len(word):])

                    if found:
                        return

            # 所有匹配方式都尝试过，仍无法拆分
            failed.add(string)

        dfs(s)
        return found == 1
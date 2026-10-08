class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        result = []
        def dfs(left, right):
            if left == right and len(path) == 2*n:
                result.append("".join(path))
            if left < n:
                path.append("(")
                dfs(left+1,right)
                path.pop()
            if right < left:
                path.append(")")
                dfs(left,right+1)
                path.pop()
        dfs(0,0)
        return result
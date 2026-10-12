class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            # 负数贡献直接舍弃，不走这一边
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # 以当前节点为转折点，可以连接左右两边
            ans = max(ans, left + node.val + right)

            # 接到父节点时，只能带上一边
            return node.val + max(left, right)

        dfs(root)
        return ans
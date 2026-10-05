class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        low = min(p.val, q.val)
        high = max(p.val, q.val)

        node = root
        while node:
            if node.val > high:
                # p 和 q 都在左子树
                node = node.left
            elif node.val < low:
                # p 和 q 都在右子树
                node = node.right
            else:
                # p、q 分居两侧，或 node 就是其中一个
                return node
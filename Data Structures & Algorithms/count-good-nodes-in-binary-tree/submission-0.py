# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        number_of_good_value = 0
        if not root:
            return number_of_good_value
        def dfs(node, largest):
            nonlocal number_of_good_value
            if node.val >= largest:
                number_of_good_value += 1
            largest = max(node.val, largest)
            if node.left:
                dfs(node.left, largest)
            if node.right:
                dfs(node.right, largest)
        dfs(root, root.val)
        return number_of_good_value
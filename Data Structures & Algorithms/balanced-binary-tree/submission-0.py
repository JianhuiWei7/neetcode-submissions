# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        def depth(node):
            nonlocal is_balanced
            if not is_balanced:
                return 0
            if not node:
                return 0
            else:
                left_depth = depth(node.left)
                right_depth = depth(node.right)
                if abs(left_depth - right_depth) > 1:
                    is_balanced = False
            return 1 + max(left_depth, right_depth)
        depth(root)
        return is_balanced
        # def is_balanced(node):
        #     left_depth = depth(node.left)
        #     right_depth = depth(node.right)
        #     if abs(left_depth - right_depth) > 1:
        #         return False
        #     else:
        #         return is_balanced(node.left) and is_balanced(node.right)
        # return is_balanced(root)

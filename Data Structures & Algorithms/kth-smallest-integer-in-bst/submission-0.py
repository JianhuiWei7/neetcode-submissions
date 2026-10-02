# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return_list = []
        def preorder(root):
            if root is None:
                return
            preorder(root.left)
            return_list.append(root.val)
            preorder(root.right)
        preorder(root)
        return return_list[k-1]
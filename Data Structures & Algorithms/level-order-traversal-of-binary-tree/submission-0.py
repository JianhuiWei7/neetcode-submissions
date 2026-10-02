# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            current_level_len = len(queue)
            current_level_out = []
            for _ in range(current_level_len):
                node = queue.popleft()
                if node:
                    current_level_out.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if current_level_out:
                result.append(current_level_out)
        return result









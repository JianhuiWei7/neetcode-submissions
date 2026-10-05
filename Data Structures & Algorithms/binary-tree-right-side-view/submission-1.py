# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if not root:
            return []
        queue.append(root)
        total_out = []
        while queue:
            len_this_level = len(queue)
            number_this_level = []
            for _ in range(len_this_level):
                current = queue.popleft()
                number_this_level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            total_out.append(number_this_level[-1])
        return total_out





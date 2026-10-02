# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(q,p):
            if q is None and p is None:
                return True
            elif q and p:
                return p.val == q.val and sameTree(p.left, q.left) and  sameTree(p.right, q.right)
            else:
                return False
        
        queue = deque()
        queue.append(root)
        while queue:
            element = queue.popleft()
            if element:
                queue.append(element.left)
                queue.append(element.right)
                if element.val == subRoot.val:
                    if sameTree(element, subRoot):
                        return True
        return False
            






        
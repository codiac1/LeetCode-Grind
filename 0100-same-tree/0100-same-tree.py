# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,p,q):
        if not p and not q :
            return True
        if not p or not q:
            return False
        if (p.val == q.val) and self.solve(p.left, q.left) and self.solve(p.right, q.right)  :
            return True
        return False
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.solve(p,q)
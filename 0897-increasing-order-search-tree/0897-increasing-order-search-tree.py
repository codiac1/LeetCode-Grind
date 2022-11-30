# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.prev = None
        
        def helper(root):
            if root.right:
                helper(root.right)
                
            root.right = self.prev
            
            if self.prev :
                self.prev.left = None
                
            self.prev = root
            
            if root.left:
                helper(root.left)
                
        helper(root)
        return self.prev
            
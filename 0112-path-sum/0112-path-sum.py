# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, node: Optional[TreeNode], target: int) -> bool:
        if not node :
            return False

        if (not node.left and not node.right ) and target - node.val == 0 :
            return True

        return self.hasPathSum(node.left , target - node.val) or self.hasPathSum(node.right , target - node.val)
        
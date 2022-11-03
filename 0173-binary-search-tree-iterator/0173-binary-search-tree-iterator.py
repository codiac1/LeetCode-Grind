# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stk = []
        
        def dfs(root):
            if not root :
                return 
            dfs(root.left)
            self.stk.append(root.val)
            dfs(root.right)
        
        dfs(root)    
        self.stk.reverse()

    def next(self) -> int:
        return self.stk.pop()

    def hasNext(self) -> bool:
        if self.stk:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
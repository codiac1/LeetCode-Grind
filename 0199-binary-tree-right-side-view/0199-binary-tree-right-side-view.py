# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        
        ans = []
        
        while(q):
            l = len(q)
            for i in range(l):
                curr = q.popleft()
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            ans.append(curr.val)
            
        return ans
        
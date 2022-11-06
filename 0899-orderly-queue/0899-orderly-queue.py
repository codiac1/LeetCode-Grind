class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))
        
        temp = s + s
        ans = s
        n = len(s)
        
        for i in range( 1, n):
            m = temp[i : i + n]
            ans = min( m , ans)
            
        return ans
        
        
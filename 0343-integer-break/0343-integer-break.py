class Solution:
    def integerBreak(self, n: int) -> int:
        def solve(num , curr):
            if (num == 1):
                return 1
            
            if (curr == 0):
                return 1
            
            if dp[num][curr] != -1 :
                return dp[num][curr]
            
            take = 0
            
            if num <= curr:
                take = num * solve(num , curr - num)
                
            notTake = solve(num-1 , curr)
            
            dp[num][curr] = max(take , notTake )
            return dp[num][curr]
        
        dp = [[-1]*(n+1) for _ in range(n+ 1)]
        
        return solve(n -1, n)
    
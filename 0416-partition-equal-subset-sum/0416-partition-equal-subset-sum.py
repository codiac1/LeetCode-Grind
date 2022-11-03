class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s&1:
            return False
        
        target = s//2
        dp = [[-1]*(target +1) for _ in range(len(nums)+1)]
        
        def knapsack(index , sum_):
            if index < 0 or sum_ > target:
                return False
            if sum_ == target:
                return True
            
            if dp[index][sum_] != -1:
                return dp[index][sum_]
            
            
            take = knapsack(index -1 , sum_ + nums[index])
            not_take  = knapsack(index -1 , sum_)
            
            dp[index ][sum_] =  take or not_take
            return dp[index] [sum_]
            
        return knapsack(len(nums)-1 , 0)
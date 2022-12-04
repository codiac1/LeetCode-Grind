class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        pre = [0]*n
        post = [0]*n
        
        pre[0] = nums[0]
        post[n-1] = nums[n-1]
        
        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i]
            post[n-i-1] = post[n-i] + nums[n-i-1]
        
        count = 0 
        
        for i in range(n-1):
            if pre[i] >= post[i+1]:
                count += 1
                
        return count
        
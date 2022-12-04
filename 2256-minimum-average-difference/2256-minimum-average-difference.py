class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        
        preSum = [0]*n
        preSum[0] = nums[0]
        
        for i in range(1,n):
            preSum[i] = preSum[i-1]+nums[i]
        
        minIdx = n
        minVal = math.inf
        
        for i in range(n):
            if i == n-1:
                v = abs(preSum[i]//(i+1) - 0)
            else:
                v = abs(preSum[i]//(i+1) - (preSum[n-1] - preSum[i])//(n-i-1))
        
            if v < minVal:
                minIdx = i
                minVal = v
                
        return minIdx
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)        
            
        for i in range(1,n):
            nums[i] +=  nums[i-1]
        
        for i in range(n):
            if i == 0 :
                x = 0 
            else:
                x = nums[i-1]
                
            if i == n-1:
                y = 0 
            else:
                y = nums[n-1] - nums[i]
            
            if x == y:
                return i
        return -1
        
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m = max(nums)
        if m < 0:
            return  1
        nums = set(nums)
        
        for ele in range(1 , m +1):
            if ele not in nums:
                return ele
            
        return m +1
            
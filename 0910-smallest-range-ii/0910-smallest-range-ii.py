class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        mn = nums[0]
        mx = nums[-1]
        
        ans = mx - mn
        
        for i in range(len(nums) - 1):
            big = max (nums[-1] , nums[i] + 2*k )
            small = min(nums[0] + 2*k , nums[i+1] )
            
            ans = min(ans , big - small)
            
        return ans
                
            
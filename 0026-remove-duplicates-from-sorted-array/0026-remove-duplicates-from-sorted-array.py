class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        j=0
        k=0
        while(j<len(nums)):
            if j+1==len(nums):
                break
            if nums[i] == nums[i-1] :
                x = nums.pop(i)
                nums.append(".")
            else:
                i+=1 
            j+=1
            
        for i in nums:
            if i != ".":
                k+=1
        return k
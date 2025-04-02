class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        temp = {}
        ans = []

        stk = []

        for i in range(n-1, -1 , -1):
            temp[nums2[i]] = -1
            while(stk and stk[-1] <= nums2[i]):
                stk.pop()

            if stk:
                temp[nums2[i]] = stk[-1]

            stk.append(nums2[i])

        print(temp)

        for num in nums1:
            ans.append(temp[num])

        return ans
        


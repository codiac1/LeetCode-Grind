class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = []
        right = []
        n = len(heights)
        stk = []

        for i in range(n):
            while(stk and heights[stk[-1]] >= heights[i]):
                stk.pop()

            if not stk :
                left.append(-1)

            else:
                left.append(stk[-1])
            stk.append(i)

        print(left)
        stk.clear()

        for i in range(n-1,-1 , -1):
            while(stk and heights[stk[-1]] >= heights[i]):
                stk.pop()

            if not stk :
                right.append(n)

            else:
                right.append(stk[-1])
            stk.append(i)

        right.reverse()
        print(right)
        ans = 0
        maxArea = 0
        for i in range(n):
            ans = (right[i] - left[i] -1) * heights[i]
            maxArea = max(ans ,maxArea)

        return maxArea




                
                
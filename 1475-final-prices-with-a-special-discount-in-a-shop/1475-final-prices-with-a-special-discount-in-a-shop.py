class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk = []
        ans = []
        
        for ele in reversed(prices):
            while(stk and ele < stk[-1]):
                stk.pop()
                
            if not stk :
                ans.append(ele)
            
            elif stk[-1] <= ele :
                ans.append(ele - stk[-1])
            stk.append(ele)
        return reversed(ans)
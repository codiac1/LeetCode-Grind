class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low  = 1
        high = max(piles)
        speed = 0

        def canEat(x):
            reqH = 0
            for ele in piles:
                reqH += ele//x
                if (ele%x) :
                    reqH += 1

            return reqH <= h
                
        while(low < high ):
            k = ( high + low ) // 2

            if canEat(k):
                high = k
            else :
                low = k + 1

        return high 

             
                
        
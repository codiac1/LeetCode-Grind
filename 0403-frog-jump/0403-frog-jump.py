class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stones1 = set(stones)
        dp = {}
        def jump (currValue , prevValue):
            k = currValue - prevValue 
            if currValue not in stones1 :
                return False

            if currValue >= stones[-1]:
                return True

            if (currValue , prevValue) in dp:
                return dp[(currValue , prevValue)]

            for j in [-1 , 0 , 1]:
                if currValue + k + j > currValue and jump(currValue + k + j, currValue):
                    dp[(currValue , prevValue)]  = True
                    return True
            dp[(currValue , prevValue)] = False
            return False
 
        if stones[1] - stones[0] > 1 :
            return False

        return jump(stones[1], stones[0])

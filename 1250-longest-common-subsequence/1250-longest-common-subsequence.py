class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def fun (x, y ):
            if x == 0 or y == 0:
                return 0 

            if dp[x-1][y-1] != -1:
                return dp[x-1][y-1]
		
            if ( text1[x-1] == text2[y -1]):
                dp[x-1][y-1] = 1 + fun(x-1, y-1)
            else:
                dp[x-1][y-1] = 0 + max(fun(x , y-1), fun(x-1 , y))

            return dp[x-1][y-1] 

        n = len(text1)
        m = len(text2)

        dp = [[-1 for _ in range(m)] for _ in range(n)]

        return fun(n, m)


        
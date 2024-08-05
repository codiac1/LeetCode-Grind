class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        if len(arr) < k :
            return ""

        d = {}

        for s in arr:
            if s not in d:
                d[s] = 0

            d[s] += 1

        for s in arr:
            if d[s] == 1:
                k -= 1
            if k == 0 :
                return s

        return ""
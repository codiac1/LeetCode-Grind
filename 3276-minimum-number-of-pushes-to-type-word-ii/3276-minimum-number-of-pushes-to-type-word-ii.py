class Solution:
    def minimumPushes(self, word: str) -> int:
        d = {}

        for ch in word:
            if ch not in d:
                d[ch] = 0 

            d[ch] += 1

        sorted_d = sorted(d.items(), key = lambda x: x[1], reverse = True)

        res = 0
        c = 1
        i = 1

        print(sorted_d)
        for ele in sorted_d:          
            print(res , "  " , c)
            res += ele[1] * c           

            if i >= 8 and i % 8 == 0 :
                c += 1
            i += 1

        return res
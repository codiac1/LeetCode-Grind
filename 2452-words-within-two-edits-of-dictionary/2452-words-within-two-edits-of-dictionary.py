class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        
        for word in queries :
            for dword in dictionary:
                count = 0 
                for i in range(len(word)):
                    if word[i] != dword[i]:
                        count += 1
                    if count > 2:
                        break
                        
                if count <= 2:
                    ans.append(word)
                    break
                    
        return ans
        
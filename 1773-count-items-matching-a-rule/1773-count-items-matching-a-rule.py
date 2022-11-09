class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {"type": 0 , "color" : 1, "name" : 2 }
        ans  =0 
        
        for ele in items :
            if ele[d[ruleKey]] == ruleValue :
                ans += 1
                
        return ans
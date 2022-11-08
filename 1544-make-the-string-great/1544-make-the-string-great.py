class Solution:
    def makeGood(self, s: str) -> str:
        stk  = []
        
        for ele in s :
            if not stk:
                stk.append(ele)
                continue
            
            elif ele.islower():
                if stk[-1].isupper() and ele.lower() == stk[-1].lower():
                    stk.pop()
                    continue
                    
            elif ele.isupper():
                if stk[-1].islower() and ele.lower() == stk[-1].lower():
                    stk.pop()
                    continue
                    
            stk.append(ele)
        
        return "".join(stk)
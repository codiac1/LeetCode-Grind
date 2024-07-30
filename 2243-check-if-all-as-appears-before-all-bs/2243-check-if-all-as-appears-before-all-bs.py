class Solution:
    def checkString(self, s: str) -> bool:
        b_count = 0 

        for ch in s:
            if ch == 'a':
                if b_count > 0 :
                    return False
            else:
                b_count += 1

        return True
        
         

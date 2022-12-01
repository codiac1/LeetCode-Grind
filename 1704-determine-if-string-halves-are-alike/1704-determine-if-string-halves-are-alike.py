class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowSet = set("aeiouAEIOU")     
        mid = len(s)//2;
        
        i = 0
        left = 0 
        right = 0 
        
        while(i< mid):
            if s[i] in vowSet:
                left += 1
            if s[i+mid] in vowSet :
                right += 1
            i += 1
            
        if left == right:
            return True
        return False
    
        
        
        
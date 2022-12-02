class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal :
            return len(set(s)) < len(s)
        
        l = 0 
        r = len(s)-1
        
        while(l < r+1 and s[l] == goal[l]):
            l+=1
            
        while(r >= 0 and s[r] == goal[r]):
            r -= 1
        
        s = list(s)
        goal = list(goal)
        
        s[l], s[r] = s[r] , s[l]
        
        return s == goal
            
        
        
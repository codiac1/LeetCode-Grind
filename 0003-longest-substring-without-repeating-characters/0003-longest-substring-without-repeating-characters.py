class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        max_sub = 0
        left = 0
        
        for right in range(len(s)):
            if s[right] in map:
                if map[s[right]] < left:
                    max_sub = max(max_sub , (right - left +1))
                else:
                    left = map[s[right]]+1
            else:
                max_sub = max(max_sub , (right - left +1))
            
            map[s[right]] = right
        
        return max_sub
            
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        
        for ele in arr:
            d[ele] = d.get(ele , 0)+1
            
        if len(set(d.values())) == len(set(arr)):
            return True
        return False
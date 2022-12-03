class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        
        for ch in s:
            d[ch] += 1
            
        ans = []    
        a = sorted(d.items() , key = lambda x: (x[1] , x[0]) , reverse = True)
        
        for k,v in a:
            ans.append(k*v)
            
        return "".join(ans)
        
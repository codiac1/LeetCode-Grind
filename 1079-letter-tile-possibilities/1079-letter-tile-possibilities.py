class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        ans = set()
        visited = set()
        
        def foo(index , s):
            if (index == n):
                return 
            
            if len(s) > 0:
                ans.add(s)  
            
            for i in range(n):
                if i in visited:
                    continue
                visited.add(i)
                foo(i , s + tiles[i])
                visited.remove(i)
        
        foo(0 , "")
        
        print(ans)
        return len(ans)
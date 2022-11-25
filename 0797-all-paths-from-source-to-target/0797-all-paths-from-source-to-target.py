class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visited = set()
        self.ans = []
        
        def dfs(node , temp):
            if node == len(graph)-1 :
                temp.append(node)
                self.ans.append(temp[:])
                
            visited.add(node)
            temp.append(node)
            
            for nbr in graph[node]:
                if nbr in visited:
                    continue
                
                dfs(nbr , temp[:])
                
            visited.remove(node)
            temp.pop()
        
        
        dfs(0 , [])
        return self.ans
                    
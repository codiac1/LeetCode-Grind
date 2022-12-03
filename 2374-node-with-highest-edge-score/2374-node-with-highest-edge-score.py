class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        ans = 0 
        graph = [0]*len(edges)
            
        for i in range(len(edges)):
            graph[edges[i]] += i
            
        #print(graph)
        mx = 0 
        
        for i in range(len(edges)):
            if graph[i] >= mx:
                mx = graph[i]
                
        for i in range(len(edges)): 
            if mx == graph[i]:
                return i
        

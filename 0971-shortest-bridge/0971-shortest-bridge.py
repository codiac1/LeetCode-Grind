from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()

        def isValid(x, y):
            if x >= n or x < 0 or y < 0 or y >= n or grid[x][y] == 2:
                return False
            return True

        def dfs(x, y):
            if not isValid(x,y) or grid[x][y] == 0 :
                return
            
            grid[x][y] = 2  
            q.append((x,y))

            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                newx = x + dx
                newy = y + dy

                dfs(newx, newy)
            
        def bfs():
            min_flips = 0

            while(q):
                level = len(q)
                for l in range(level):
                    x, y = q.popleft()
                    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        newx = x + dx
                        newy = y + dy

                        if not isValid(newx, newy):
                            continue

                        if grid[newx][newy] == 1:
                            return min_flips
                        grid[newx][newy] = 2 
                        q.append((newx, newy))

                min_flips += 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i , j)
                    return bfs()

        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 
        n = len(grid)
        m = len(grid[0])
        visited = set()

        def isInvalid(i ,j ):
            return i >= n or i < 0 or j >= m or j < 0 or ((i, j) in visited)

        def dfs(i , j):
            visited.add((i , j))

            for dx , dy in [[-1, 0] , [1, 0], [0 , -1], [0 ,1]]:
                nx = i + dx
                ny = j + dy

                if isInvalid(nx , ny):
                    continue

                if grid[nx][ny] == "1":
                    dfs(nx , ny)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i , j )
                    islands += 1

        return islands

    

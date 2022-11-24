class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r = len(board)
        c = len(board[0])
        
        def Valid(x, y):
            if x < r and x >= 0 and y < c and y >= 0 and board[x][y] == "O":
                return True
            return False
        
        
        def dfs(i , j):
            board[i][j] = "m"
            for dx , dy in [(-1 , 0), (1 , 0) , (0 , 1) , (0 , -1)]:
                nx = i + dx
                ny = j + dy
                
                if not Valid(nx , ny):
                    continue
                    
                dfs(nx , ny)
        
        for i in range(r):
            if board[i][0] == "O":
                dfs(i , 0) 
            if board[i][c-1] == "O":
                dfs(i , c-1)
                
        for j in range(c):
            if board[0][j] == "O":
                dfs(0 , j) 
            if board[r-1][j] == "O":
                dfs(r-1 , j)
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "m":
                    board[i][j] = "O"
                
                    
        
        
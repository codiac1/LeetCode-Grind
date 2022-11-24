class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def Valid(x , y):
            if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and board[x][y] != ".":
                return True
            return False
            
        def dfs(i , j):
            board[i][j] = "."
            
            for dx , dy in [(1 , 0), (0 , 1) , (-1 , 0) , (0 , -1)]:
                nx = i + dx
                ny = j + dy
                
                if not Valid(nx , ny):
                    continue
                    
                dfs(nx , ny)
        
        count = 0 
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    dfs(i ,j)
                    count += 1
                    
        return count
                
                
                
                
/**
 * @param {number[][]} grid
 * @return {number}
 */
var numEnclaves = function(grid) {
    const n = grid.length;
    const m = grid[0].length;
    
    let direc = [[0 , 1] , [1 , 0] , [-1 , 0] , [0 , -1]];
    
    function dfs(x , y){
        grid[x][y] = 0
        
        for (let [dx , dy] of direc){
            let nx = x + dx;
            let ny = y + dy;
            
            if (nx <0 || nx >= n || ny < 0 || ny >= m || grid[nx][ny] != 1)
                continue;
            
            dfs(nx , ny);
        }
    }
    
    for( let i =0 ; i < n ; i++){
        if (grid[i][0] == 1)
            dfs(i , 0);
        
        if (grid[i][m-1] == 1)
            dfs(i , m-1)
        
    }
    
    for(let j = 0  ; j <m ; j++){
        if (grid[0][j] == 1)
            dfs(0 , j)
        
        if (grid[n-1][j] == 1)
            dfs(n-1 , j)
    }
    let c = 0 ;
    
    for ( let i = 0 ; i < n ; i++){
        for (let j = 0 ; j < m ; j++){
            if (grid[i][j] == 1)
                c += 1;
        }
    }
    return c ;
};
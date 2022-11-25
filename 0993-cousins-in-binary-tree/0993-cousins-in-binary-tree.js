/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} x
 * @param {number} y
 * @return {boolean}
 */
var isCousins = function(root, x, y) {
    depthX = 0;
    depthY = 0;
    
    pX = null;
    pY = null;
    
    q = [] ;   
    q.push([root , root]);
    
    depth = 0 ;
    
    while(q.length > 0){
        l = q.length;
        
        for (i = 0 ; i < l ; i++){
            [curr , parent] = q.shift();
        
            if (curr.val === x){
                depthX = depth
                pX = parent
            }
        
            if (curr.val === y){
                depthY = depth
                pY = parent
            }
            
            if (curr.left)
                q.push([curr.left , curr])
        
            if (curr.right )
                q.push([curr.right , curr])
        } 
        
        depth++;        
    }
    if ((depthX === depthY ) && ( pX != pY )) 
        return true;
    return false;
    
};
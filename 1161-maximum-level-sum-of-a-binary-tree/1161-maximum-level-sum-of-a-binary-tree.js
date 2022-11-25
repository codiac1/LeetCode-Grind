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
 * @return {number}
 */
var maxLevelSum = function(root) {
    level  = 1
    q = [];
    q.push(root)
    
    ans = 0 
    prev = Number.NEGATIVE_INFINITY;
    
    while(q.length > 0){
        l = q.length;
        s = 0;
        
        for( let i = 0 ; i < l ; i++){
            curr = q.shift();
            s += curr.val;
            
            if (curr.left) q.push(curr.left);
            
            if (curr.right) q.push(curr.right);
        }
        
        if (s > prev){
            prev = s
            ans = level
        }
        
        
       level++;  
    }
    
   return ans;
};
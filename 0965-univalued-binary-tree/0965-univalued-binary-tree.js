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
 * @return {boolean}
 */
var isUnivalTree = function(root) {
    var val =  root.val;
    function dfs(root){
        if (!root)
            return true;
        
        if (root.val != val)
            return false;
        
        return dfs(root.left) && dfs(root.right);
    }
      
    return dfs(root);
};
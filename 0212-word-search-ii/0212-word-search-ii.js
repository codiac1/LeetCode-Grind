/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(board, words) {
  const res = [], trie = {};
  
  for (let word of words) {
    let curNode = trie;
    for (let char of word) {
      curNode[char] = curNode[char] || {};
      curNode[char].count = curNode[char].count + 1 || 1;
      curNode = curNode[char];
    };
    curNode.end = word;
  }
  
  for (let row = 0; row < board.length; row++) {
    for (let col = 0; col < board[row].length; col++) {
      if (trie[board[row][col]]) traverse(row, col);
    }
  }
  
  return res;
  
  function traverse(row, col, node = trie) {
    if (!board[row][col]) return;
    
    const char = board[row][col], curNode = node[char];
    if (!curNode) return;
    
    if (curNode.end) {
      res.push(curNode.end);
      let toDelete = trie;
      for (let char of curNode.end) {
        toDelete[char].count--;
        if (!toDelete[char].count) {
          delete(toDelete[char]);
          break;
        }
        toDelete = toDelete[char];
      }
      curNode.end = null;
    }
    
    board[row][col] = 0;
    (col - 1 >= 0) && traverse(row, col - 1, curNode);
    (col + 1 < board[row].length) && traverse(row, col + 1, curNode);
    (row - 1 >= 0) && traverse(row - 1, col, curNode);
    (row + 1 < board.length) && traverse(row + 1, col, curNode);
    board[row][col] = char;
  }
};
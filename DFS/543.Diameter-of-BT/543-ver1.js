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
var diameterOfBinaryTree = function (root) {
  let result = 0;
  // let left = findOne(root.left);
  // let right = findOne(root.right);

  var findOne = function (root) {
    if (!root) return 0;
    let left = findOne(root.left);
    let right = findOne(root.right);

    result = Math.max(result, left + right);
    return 1 + Math.max(left, right);
  };

  findOne(root);

  return result;
};

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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (root, k) {
  // console.log(inOrderTraversal(root, []))
  return inOrderTraversal(root, [])[k - 1];
};

var inOrderTraversal = function (root, arr) {
  if (root === null) return;
  inOrderTraversal(root.left, arr);
  arr.push(root.val);
  inOrderTraversal(root.right, arr);
  return arr;
};

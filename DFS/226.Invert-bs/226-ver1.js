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
 * @return {TreeNode}
 */

// iterate
var invertTree = function (root) {
  let stack = [root];

  while (stack.length > 0) {
    let root = stack.pop();
    let left = root.left;
    let right = root.right;

    root.left = right;
    root.right = left;

    if (left) stack.push(left);
    if (right) stack.push(right);
  }

  return root;
};

// recursive
var invertTree = function (root) {
  if (!root) return null;

  let left = invertTree(root.left);
  let right = invertTree(root.right);

  root.left = right;
  root.right = left;

  return root;
};

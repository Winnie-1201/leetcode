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

// in order traverse;
var isValidBST = function (root) {
  // inOrder
  let prev = -Infinity;
  let result = true;
  var inOrder = function (root) {
    if (!root) return;
    // traverse left to find the left most
    inOrder(root.left);

    // do the thing
    if (root.val <= prev) result = false;
    prev = root.val;

    // traverse right
    inOrder(root.right);
  };

  inOrder(root);

  return result;
};

// use stack
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
var isValidBST = function (root) {
  // [min, max, root]
  let stack = [[-Infinity, Infinity, root]];

  while (stack.length > 0) {
    let [min, max, root] = stack.pop();
    if (!root) continue;
    if (root.val <= min) return false;
    if (root.val >= max) return false;
    stack.push([root.val, max, root.right], [min, root.val, root.left]);
  }
  return true;
};

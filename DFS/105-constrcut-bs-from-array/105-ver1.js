/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {
  // let node = new TreeNode(preorder[0])
  let preoderIndex = 0;
  let map = new Map();
  for (let i = 0; i < inorder.length; i++) {
    map.set(inorder[i], i);
  }

  var arrayToTree = function (preorder, left, right) {
    // console.log(left, right)
    if (left > right) return null;

    let node = new TreeNode(preorder[preoderIndex]);
    let mid = map.get(preorder[preoderIndex]);
    preoderIndex++;

    node.left = arrayToTree(preorder, left, mid - 1);
    node.right = arrayToTree(preorder, mid + 1, right);

    return node;
  };

  return arrayToTree(preorder, 0, preorder.length - 1);
};

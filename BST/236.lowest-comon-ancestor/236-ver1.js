/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  if (!root) return null;
  // let lca = Infinity;
  while (root) {
    if (
      (root.val <= p.val && root.val >= q.val) ||
      (root.val >= p.val && root.val <= q.val)
    ) {
      return root;
    } else if (root.val < p.val && root.val < q.val) {
      if ((root.left && root.left === p) || (root.right && root.right === q))
        return root;
      else return lowestCommonAncestor(root.right, p, q);
    } else {
      if (root.val === p.val || root.val === q.val) return root;
      return lowestCommonAncestor(root.left, p, q);
    }
  }
};

// it works!!

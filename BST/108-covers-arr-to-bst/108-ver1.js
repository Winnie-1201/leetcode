/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function (nums) {
  if (nums.length == 0) return null;
  if (nums.length == 1) return new TreeNode(nums[0]);

  let left = 0;
  let right = nums.length - 1;
  let mid = Math.floor((left + right) / 2);

  let result = new TreeNode(nums[mid]);
  result.left = sortedArrayToBST(nums.slice(0, mid));
  result.right = sortedArrayToBST(nums.slice(mid + 1));

  return result;
};

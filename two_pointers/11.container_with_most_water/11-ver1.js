/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let start = 0;
  let end = height.length - 1;
  let max = 0;
  while (start < end) {
    let temp = (end - start) * Math.min(height[start], height[end]);
    if (temp > max) max = temp;
    if (height[end] > height[start]) {
      start++;
    } else {
      end--;
    }
  }
  return max;
};

// it works~
// next time try to refactor it or use other methods;

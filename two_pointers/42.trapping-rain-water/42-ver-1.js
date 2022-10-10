/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
  let left = height[0] === 0 ? 1 : 0;
  let right = left === 0 ? 0 : 1;
  let sum = 0;
  while (right < height.length) {
    if (height[right] <= height[left]) {
      right++;
    } else if (height[right] > height[left] || right === height.length - 1) {
      // console.log(right - left - 1)
      sum += (right - left - 1) * Math.min(height[left], height[right]);
      // console.log(sum)
      while (left < right - 1) {
        left++;
        sum -= height[left];
      }
      left++;
      right++;
    }
  }
  return sum;
};

// it passed some of the cases;
// but my method can not deal with the case like: [3, 2, 1, 2, 1];
// use two pointers with left and right; right = size - 1;
// and use leftmax and rightmax to store the higher bar and to do the calculation;

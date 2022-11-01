/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
  let left = 1;
  let right = x;
  if (x === 0) return 0;
  while (left < right) {
    let mid = Math.floor((left + right) / 2);
    if (mid * mid <= x && (mid + 1) * (mid + 1) > x) return mid;
    else if (mid * mid > x) right = mid - 1;
    else left = mid + 1;
  }
  return left;
};

// other people's method
/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
  let left = 0;
  let right = Math.floor((1 + x) / 2);
  while (left < right) {
    let mid = Math.floor((left + right + 1) / 2);
    if (mid * mid > x) right = mid - 1;
    else left = mid;
  }
  return left;
};

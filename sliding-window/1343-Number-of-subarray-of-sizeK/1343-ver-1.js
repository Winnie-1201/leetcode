/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} threshold
 * @return {number}
 */
var numOfSubarrays = function (arr, k, threshold) {
  let count = 0;
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
    if (i >= k - 1) {
      if (sum / k >= threshold) {
        count++;
        sum -= arr[i - k + 1];
      } else sum -= arr[i - k + 1];
    }
  }
  return count;
};

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  let map = new Map();
  let count = 0;
  let start = 0;
  let maxCount = 0;
  for (let i = 0; i < s.length; i++) {
    map.set(s[i], map.get(s[i]) + 1 || 1);
    count = count > map.get(s[i]) ? count : map.get(s[i]);
    if (i - start + 1 - count > k) {
      map.set(s[start], map.get(s[start]) - 1);
      start++;
    }
    maxCount = Math.max(maxCount, i - start + 1);
  }
  return maxCount;
};

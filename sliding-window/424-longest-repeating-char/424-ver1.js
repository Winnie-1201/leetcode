/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  let map = {};
  let maxCount = 0;
  let start = 0;
  let maxLen = 0;
  for (let end = 0; end < s.length; end++) {
    map[s[end]] = (map[s[end]] || 0) + 1;
    maxCount = maxCount > map[s[end]] ? maxCount : map[s[end]];
    // if meet the first char that is different from the previous
    // then end - start + 1 will be greater than maxCount;
    // if end - start + 1 - maxCount > k, then means there is no more
    // available flip;
    // then we need to shrink the window
    // and decrease the value of the removed char (which is the first letter at start)
    if (end - start + 1 - maxCount > k) {
      map[s[start]] -= 1;
      start++;
    }
    maxLen = maxLen > end - start + 1 ? maxLen : end - start + 1;
  }
};

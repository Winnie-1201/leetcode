/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  if (s.length <= 1) return s.length;
  let set = new Set(s[0]);
  let start = 0;
  let end = 1;
  let count = 0;
  while (end < s.length) {
    if (!set.has(s[end])) {
      set.add(s[end]);
      end++;
      count = Math.max(count, end - start);
    } else {
      set.delete(s[start]);
      start++;
      // set.add(s[end]);
      // end++;
    }
  }
  return count;
};

// using set and sliding window
// using set instead of arr because the add and delete are constant time
// shrink the window when there is a duplicate

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubstring = function (s, k) {
  return longest(s, 0, s.length, k);
};

var longest = function (s, start, end, k) {
  if (end < k) return 0;
  let map = new Map();
  for (let i = start; i < end; i++) {
    map.set(s[i], map.get(s[i]) + 1 || 1);
  }

  for (let i = start; i < end; i++) {
    // if all elements in map qualify, then return end-start
    if (map.get(s[i]) >= k) continue;
    // if not qualify, then divide untill all qualify
    let next = i + 1;
    while (next < end && map.get(s[next]) < k) next++;
    // second is here
    // return the larger end-start
    return Math.max(longest(s, start, i, k), longest(s, next, end, k));
  }

  // first goes here
  return end - start;
};

// method: divide and conquer
// first divide the problem into small problem (each problem should solve the same question)
// then combine all the solution

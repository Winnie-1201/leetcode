/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubstring = function (s, k) {
  //  let obj = {};
  //  for (let i = 0; i < s.length; i++) {
  //      if (obj[s[i]]) obj[s[i]]++;
  //      else obj[s[i]] = 1;
  //  };
  //  let arr = [];
  //  for (let key in obj) {
  //      if (obj[key] >= k) arr.push(key);
  //  }
  //  let count = 0;
  // for (let i = 0; i < s.length; i++) {
  //     if (arr.includes(s[i])) count++;
  //     else break;
  // }
  //  return count;
};

// it only works for few cases;
// an idea: next time maybe try:
// 1. use start points at the first one, find how may duplicates, slices it
//    verify if this substring qualify, if so, mark the length;
// 2. increase start;
//
// next time, take a look of the recursive method;

/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function (s, p) {
  let size = s.length - p.length;
  let res = [];
  for (let i = 0; i < size + 1; i++) {
    let sub = s.slice(i, i + p.length);
    if (isAnagram(sub, p)) res.push(i);
  }
  return res;
};

var isAnagram = function (subString, p) {
  subString = subString.split("").sort();
  p = p.split("").sort();
  for (let i = 0; i < subString.length; i++) {
    if (subString[i] !== p[i]) return false;
  }
  return true;
};

// only works for few cases;
// Time limit exceeded;
// next itme:
// use sliding window

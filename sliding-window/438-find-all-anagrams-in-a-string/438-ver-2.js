/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function (s, p) {
  let temp = new Map();
  let size = p.length;
  for (let i = 0; i < size; i++) {
    // temp[s[i]] = (temp[s[i]] || 0) + 1
    if (temp.get(p[i])) temp.set(p[i], temp.get(p[i]) + 1);
    else temp.set(p[i], 1);
  }
  let sub = new Map();
  let res = [];
  for (let i = 0; i < s.length; i++) {
    if (sub.get(s[i])) sub.set(s[i], sub.get(s[i]) + 1);
    else sub.set(s[i], 1);
    if (i >= size - 1) {
      if (equalMap(sub, temp)) {
        res.push(i - size + 1);
        if (sub.get(s[i - size + 1]) > 1)
          sub.set(s[i - size + 1], sub.get(s[i - size + 1]) - 1);
        else sub.delete(s[i - size + 1]);
      } else {
        if (sub.get(s[i - size + 1]) > 1) {
          sub.set(s[i - size + 1], sub.get(s[i - size + 1]) - 1);
        } else sub.delete(s[i - size + 1]);
      }
    }
  }
  return res;
};

var equalMap = function (map1, map2) {
  var testVal;
  if (map1.size !== map2.size) {
    return false;
  }
  for (var [key, val] of map1) {
    testVal = map2.get(key);
    // in cases of an undefined value, make sure the key
    // actually exists on the object so there are no false positives
    if (testVal !== val || (testVal === undefined && !map2.has(key))) {
      return false;
    }
  }
  return true;
};
// var isAnagram = function(subString, p) {
//     subString = subString.split("").sort();
//     p = p.split("").sort();
//     for (let i = 0; i < subString.length; i++) {
//         if (subString[i] !== p[i]) return false;
//     }
//     return true;
// }

// DO NOT forget to write the "else";
// sometime it does not work for not explicitly writing the else clause;
// next time:
// try other method;

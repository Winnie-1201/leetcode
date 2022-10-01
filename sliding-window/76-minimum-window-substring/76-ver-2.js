/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
  let windowStart = 0;
  let minSub = "";
  let map = new Map();
  for (let i = 0; i < t.length; i++) {
    map.set(t[i], (map.get(t[i]) || 0) + 1);
  }
  let obj = new Map();
  let samp = "";
  for (let i = 0; i < s.length; i++) {
    samp += s[i];
    if (map.has(s[i])) {
      obj.set(s[i], (obj.get(s[i]) || 0) + 1);
    }
    while (map.size === obj.size && mapCompare(obj, map)) {
      minSub = minSub.length === 0 ? samp : minSub;
      minSub = minSub.length >= samp.length ? samp : minSub;
      if (obj.get(s[windowStart]) > 1) {
        obj.set(s[windowStart], obj.get(s[windowStart]) - 1);
      } else obj.delete(s[windowStart]);
      samp = samp.substring(1);
      windowStart++;
    }
  }
  return minSub;
};

var mapCompare = function (map1, map2) {
  for (let [key, value] of map1) {
    if (value < map2.get(key)) return false;
  }
  return true;
};

// it works but slow;
// next time:
// maybe there is no need to create the string to store the characters;
// can use the substring with index method to get the substring;
// try to use {} to create the hash map instead.

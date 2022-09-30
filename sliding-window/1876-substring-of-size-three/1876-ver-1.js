/**
 * @param {string} s
 * @return {number}
 */
var countGoodSubstrings = function (s) {
  let count = 0;
  let map = {};
  for (let i = 0; i < s.length; i++) {
    map[s[i]] = (map[s[i]] || 0) + 1;
    if (i >= 2) {
      // console.log(map)
      if (Object.keys(map).length === 3) {
        count++;
        delete map[s[i - 2]];
      } else {
        if (map[s[i - 2]] > 1) {
          map[s[i - 2]] -= 1;
        } else {
          delete map[s[i - 2]];
        }
      }
    }
  }
  return count;
};

// it works;
// next time:
// 1.
// can also use set to check:
// get the three characters and put it in new Set(),
// then to check its length

/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function (s, p) {
  let map = new Map();
  for (let i = 0; i < p.length; i++) {
    map.set(p[i], map.get(p[i]) + 1 || 1);
  }

  let tempMap = new Map();
  let result = [];
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    tempMap.set(s[i], tempMap.get(s[i]) + 1 || 1);
    if (tempMap.get(s[i]) <= map.get(s[i]) && map.get(s[i])) {
      count += 1;
    }

    let remove = i - p.length + 1;
    if (i >= p.length - 1) {
      if (count === p.length && map.size === tempMap.size) {
        count -= 1;
        result.push(remove);
        if (tempMap.get(s[remove]) > 1) {
          tempMap.set(s[remove], tempMap.get(s[remove]) - 1);
        } else {
          tempMap.delete(s[remove]);
        }
      } else {
        if (tempMap.get(s[remove]) > 1) {
          if (tempMap.get(s[remove]) <= map.get(s[remove])) count -= 1;
          tempMap.set(s[remove], tempMap.get(s[remove]) - 1);
        } else {
          tempMap.delete(s[remove]);
          if (map.get(s[remove])) count -= 1;
        }
      }
    }
  }
  return result;
};

// slow but works!
// for next time, tried to use a helper funciton;

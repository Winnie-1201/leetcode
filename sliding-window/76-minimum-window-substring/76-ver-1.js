/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
  if (t.length > s.length || (s.length === t.length && s !== t)) return "";
  if (s === t) return s;
  let set = new Set(t.split(""));
  let result = "";
  for (let i = 0; i < s.length - t.length; i++) {
    let temp = "";
    let count = set.size;
    let j = i;
    while (count >= 1 && j < s.length) {
      // console.log(set, s[j])
      if (set.has(s[j])) {
        count--;
        temp += s[j];
        j++;
      } else if (!set.has(s[j]) && temp.length !== 0) {
        temp += s[j];
        j++;
      } else {
        j++;
      }
    }
    if (temp && result) {
      result = result.length >= temp.length ? temp : result;
    } else if (temp) {
      result = temp;
    }
  }
  return result;
};

// Only works for few cases;
// Not that familiar with sliding window in the character cases;
// for next time:
// watch more video about how to deal with character problems using
// sliding window

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let start = 0;
  let max = 0;
  if (s.length <= 1) return s.length;
  while (start < s.length - 1) {
    let temp = s[start];
    let nxt = start + 1;
    while (nxt < s.length) {
      if (!temp.includes(s[nxt])) {
        temp += s[nxt];
        nxt++;
      } else break;
    }
    // console.log(temp)
    max = temp.length > max ? temp.length : max;
    start++;
  }
  return max;
};

// i think this is the sliding window problem also;
// but i used other method and it works;
//
// next time, try other method

/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function (s) {
  if (s.length <= 1) return s.length;
  s = s.split("").sort().join("");
  let count = 0;
  let count_sig = s.length % 2 === 0 ? 0 : 1;
  let i = 0;
  while (i < s.length - 1) {
    if (s[i] === s[i + 1]) {
      count += 2;
      i += 2;
    } else {
      count_sig = 1;
      i++;
    }
  }
  return count + count_sig;
};

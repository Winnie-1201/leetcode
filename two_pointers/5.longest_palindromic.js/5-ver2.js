/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  let longest = 0;
  let leftPalindrome = 0;
  let rightPalindrome = 0;

  var findLongest = function (left, right) {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      left -= 1;
      right += 1;
    }

    // longest = (right - 1) - (left + 1) + 1 > longest ? (right - 1) - (left + 1) + 1 : longest
    if (right - 1 - (left + 1) + 1 > longest) {
      longest = right - 1 - (left + 1) + 1;
      leftPalindrome = left + 1;
      rightPalindrome = right - 1;
    }
  };

  for (let i = 0; i < s.length; i++) {
    // for even palindrome
    findLongest(i, i + 1);
    // for odd palindrom
    findLongest(i, i);

    if ((s.length - i) * 2 <= longest) break;
  }

  return s.slice(leftPalindrome, rightPalindrome + 1);
};

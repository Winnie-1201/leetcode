/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  if (s.length <= 1) return s;
  let res = s[0];
  for (let i = 0; i < s.length; i++) {
    let start = s[i];
    let arr = s.split("");
    // console.log(arr);
    let end = arr.findLastIndex((el) => el === start);
    if (end > i) {
      let str = s.slice(i, end + 1);
      if (isPalindrome(str) && str.length > res.length) {
        res = str;
      }
    }
  }
  return res;
};

var isPalindrome = function (s) {
  s = s.replace(/[^a-zA-Z0-9]+/g, "").toLowerCase();
  for (let i = 0; i < s.length / 2; i++) {
    if (s[i] !== s[s.length - i - 1]) return false;
  }
  return true;
};

console.log(longestPalindrome("ccc"));

// i dont know why this does not work on leetcode;
// but it works here for the findLastIndex

// below is another method from thoers:
/**
 * *Time: O(N^2)
 * *Space: O(1)
 */
// Runtime: 95 ms, faster than 96.60% of JavaScript online submissions for Longest Palindromic Substring.
// Memory Usage: 45 MB, less than 72.60% of JavaScript online submissions for Longest Palindromic Substring.
const longestPalindrome = (s) => {
  let output = "";

  // expand from center to left and right to find longest palindrome
  const findPalindrome = (i, j) => {
    // handle out of bounds: i >= 0 AND j < N
    // check if two values match
    while (i >= 0 && j < s.length && s[i] === s[j]) {
      i--;
      j++;
    }

    return s.slice(i + 1, j); // return palindrome;
  };

  // odd: both starts at current, so we don't miss one charactered palindrome
  // even: starts by comparing current character and right character
  for (let i = 0; i < s.length; i++) {
    // expand left and right from center(current index) to find longest palindrome
    const odd = findPalindrome(i, i); // handle odd length palindromes
    const even = findPalindrome(i, i + 1); // handle even length palindromes

    // get current longest palindrome
    const current = odd.length > even.length ? odd : even;

    // update longest palindrome
    if (current.length > output.length) {
      output = current;
    }
  }

  return output;
};

// first find the palidrome start from each s[i];
// then expand it from i to i-1 and i+1 untill [.., i, ...]
// not qualified for palidrome;

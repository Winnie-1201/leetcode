/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  let max = 0;

  for (let i = 0; i < s.length - 1; i++) {
    let count = 1;
    let temp = k;
    for (let j = i + 1; j < s.length; j++) {
      if (s[i] !== s[j]) {
        // console.log(temp)
        if (temp <= 0) {
          max = count > max ? count : max;
          break;
        }
        temp--;
        count++;
        // console.log(temp)
      } else count++;
    }
    max = count > max ? count : max;
    temp = k;
  }
  return max;
};

// works for 33/37 cases;
// it does not work for the case with one distinct character
// at the beginning;
//
// next time: it is a sliding window problem;
// so study for it;

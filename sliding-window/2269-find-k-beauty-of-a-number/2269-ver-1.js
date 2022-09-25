/**
 * @param {number} num
 * @param {number} k
 * @return {number}
 */
var divisorSubstrings = function (num, k) {
  let numString = String(num).split("");
  let sub = "";
  let res = 0;
  for (let i = 0; i < numString.length; i++) {
    sub += numString[i];
    if (i >= k - 1) {
      // console.log(sub)
      let temp = parseInt(sub);
      if (num % temp === 0 && temp !== 0) res++;
      if (k === 1) sub = "";
      sub = String(Number(sub) % Math.pow(10, k - 1));
    }
  }
  return res;
};

// works
// there is a built-in method in js to find the substring called substr(start, leng)

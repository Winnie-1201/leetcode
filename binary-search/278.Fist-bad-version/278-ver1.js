/**
 * Definition for isBadVersion()
 *
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function (isBadVersion) {
  /**
   * @param {integer} n Total versions
   * @return {integer} The first bad version
   */
  return function (n) {
    let left = 1;
    let right = n;
    while (left <= right) {
      let mid = Math.floor((left + right) / 2);
      // if (isBadVersion(left)) return left;
      if (isBadVersion(mid)) right = mid - 1;
      else left = mid + 1;
    }
    return left;
    // let start = 1;
    // let end = n;
    // while (start <= end) {
    //     let mid = Math.floor((start + end) / 2);
    //     if (!isBadVersion(mid)) {
    //         start = mid + 1;
    //     }
    //     else {
    //         end = mid - 1;
    //     }
    // }
    // return start;
  };
};

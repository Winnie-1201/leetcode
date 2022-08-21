/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
  let res = [];
  if (intervals.length <= 1) return intervals;
  let i = 0;
  let j = 1;
  while (i < intervals.length && j < intervals.length) {
    let val1 = intervals[i][1];
    let val2 = intervals[j][0];
    let val3 = intervals[j][1];
    if (val1 < val2) {
      res.push(intervals[i]);
      i++;
    } else if (val1 >= val2 && val1 <= val3) {
      res.push([intervals[i][0], val3]);
      i += 2;
      j += 2;
    } else {
      j++;
    }
  }
  return res;
};

// Passed some of the test;
// But my method is not that efficient and
// more like a case by case method:
// I listed out the cases and write them out in js.
// input:    [[1, 4], [0, 4]]
// output:   [[1, 4]]
// expected: [[0, 4]]
//
// maybe try to sort the array by the first element => use two pointer?

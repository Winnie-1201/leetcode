var merge = function (intervals) {
  intervals.sort((a, b) => a[0] - b[0]);
  let i = 0;
  let res = [];
  while (i < intervals.length - 1) {
    if (intervals[i][1] >= intervals[i + 1][0]) {
      intervals[i + 1][1] = Math.max(intervals[i][1], intervals[i + 1][1]);
      intervals[i + 1][0] = intervals[i][0];
      i++;
    } else {
      res.push(intervals[i]);
      i++;
    }
  }
  res.push(intervals[intervals.length - 1]);
  return res;
};

// Got it work!!!!//
// so excited!!

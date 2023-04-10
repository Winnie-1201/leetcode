from ast import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set([n for n in nums])
        for n in nums:
            cnt = 1
            if n - 1 not in numSet:
                temp = n + 1
                while temp in numSet:
                    temp += 1
                    cnt += 1
            res = max(cnt, res)
        return res

        # Time Limit Exceeded
        # res = 0
        # numSet = set([n for n in nums])
        # # print(numSet)
        # for n in nums:
        #     temp = n + 1
        #     cnt = 1
        #     while temp in numSet:
        #         cnt += 1
        #         temp += 1
        #     res = max(res, cnt)
        # return res

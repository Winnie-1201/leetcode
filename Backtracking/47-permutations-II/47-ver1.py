from ast import List
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, counter):
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for num in counter:
                if counter[num] > 0:
                    # add the current number to the perm
                    perm.append(num)
                    counter[num] -= 1
                    backtrack(perm, counter)
                    # revert it back for the next exploration
                    perm.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))
        return res

#         res = []
#         numSet = set(nums)
#         # perm = []

#         if len(nums) == 1:
#             return [nums[:]]

#         for i in range(len(numSet)):
#             first = nums.pop(0)

#             perms = self.permuteUnique(nums)

#             for perm in perms:
#                 perm.append(first)

#             res.extend(perms)
#             nums.append(first)

#         return res

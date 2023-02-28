from ast import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # current subset
        subset = []

        def dfs(idx):
            if idx >= len(nums):
                # since subset is changing, then needs to append its copy
                res.append(subset.copy())
                return

            # decision to append nums[idx]:
            subset.append(nums[idx])
            dfs(idx + 1)

            # decision not to append nums[idx]
            subset.pop()
            dfs(idx + 1)

        dfs(0)
        return res

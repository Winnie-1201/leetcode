from ast import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtract(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return

            if sum(subset) > target or i == len(candidates):
                return

            # if i == len(candidates):
            #     if sum(subset) == target:
            #         res.append(subset.copy())
            #     return

            subset.append(candidates[i])
            backtract(i)

            subset.pop()
            backtract(i + 1)

        backtract(0)
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

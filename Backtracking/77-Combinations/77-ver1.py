from ast import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(idx):
            if len(comb) == k:
                res.append(comb[:])

            for i in range(idx + 1, n + 1):
                comb.append(i)
                backtrack(i)

                comb.pop()

        backtrack(0)
        return res

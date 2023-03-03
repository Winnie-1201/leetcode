from ast import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtrack(idx):
            if idx == len(s):
                res.append(part[:])
                return

            for j in range(idx, len(s)):
                if self.isPalind(s, idx, j):
                    part.append(s[idx:j+1])

                    backtrack(j + 1)
                    part.pop()
        backtrack(0)
        return res

    def isPalind(self, s, l, r):

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

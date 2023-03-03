from ast import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        letter = {"2": ["a", "b", "c"],
                  "3": ["d", "e", "f"],
                  "4": ["g", "h", "i"],
                  "5": ["j", "k", "l"],
                  "6": ["m", "n", "o"],
                  "7": ["p", "q", "r", "s"],
                  "8": ["t", "u", "v"],
                  "9": ["w", "x", "y", "z"],
                  }

        comb = []
        for d in digits:
            comb.append(letter[d])

        res = []
        temp = []

        def backtrack(idx):
            # each element's length should be the length of digits
            if idx == len(comb):
                res.append("".join(temp[:]))
                return

            # temp += comb[0]

            # the combination length should be len(ele) * len(digits)
            for j in range(len(comb[idx])):
                temp.append(comb[idx][j])
                backtrack(idx + 1)
                temp.pop()

        backtrack(0)

        return res


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res

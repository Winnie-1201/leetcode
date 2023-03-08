class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            # for the odd length
            start, end = i, i

            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end - start + 1 > len(res):
                    res = s[start: end + 1]

                start -= 1
                end += 1

            # for the even length
            start, end = i, i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end - start + 1 > len(res):
                    res = s[start: end + 1]

                start -= 1
                end += 1

        return res

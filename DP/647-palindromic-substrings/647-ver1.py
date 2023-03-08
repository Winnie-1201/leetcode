class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            start, end = i, i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                res += 1
                start -= 1
                end += 1

            start, end = i, i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                res += 1
                start -= 1
                end += 1
        return res

        # the dp solution
        # pal = [[None]*len(s) for _ in range(len(s))]
        # ans = 0

        # # Setting single-character palindromes:
        # for i in range(len(s)):
        #     pal[i][i] = True
        #     ans += 1

        # # Checking for other palindromes:
        # for i in range(len(s)-1, -1, -1):
        #     for j in range(len(s)-1, i, -1):
        #         if s[i] == s[j] and pal[i+1][j-1] != False:
        #             pal[i][j] = True
        #             ans += 1
        #         else:
        #             pal[i][j] = False

        # # Print all found palindromes:
        # # for i in range(len(s)):
        # #     for j in range(i, len(s)):
        # #         if pal[i][j]:
        # #             print(s[i:j+1])
        # return ans

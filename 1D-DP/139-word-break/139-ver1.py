from ast import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # create a dp array to store whether
        # the word started by i is in the wordDict
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        # bottom up
        for i in range(len(s) - 1, -1, -1):
            # needs to check every word in the wordDict
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                # if one is found
                # then no need to check other words
                if dp[i]:
                    break
        return dp[0]

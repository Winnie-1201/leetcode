class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # input: "abcde" "ace"
        dp = [[0] * (len(text1) + 1) for n in range(len(text2) + 1)]
        # print(dp)
        # [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        for i in range(len(text2) - 1, -1, -1):
            for j in range(len(text1) - 1, -1, -1):
                if text1[j] == text2[i]:
                    # print(i, j, dp)
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        # print(dp)
        return dp[0][0]

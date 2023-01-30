class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # sliding window solution
        # use set because the lookup time is O(1)
        # charSet = set()
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     res = max(res, r - l + 1)
        # return res

        # my solution
        if len(s) <= 1:
            return len(s)
        maxLen = 0

        for i in range(len(s)-1):

            temp = s[i]
            start = i+1

            while start < len(s) and s[start] not in temp:
                # print(temp)
                temp += s[start]
                start += 1

            maxLen = max(len(temp), maxLen)

        return maxLen

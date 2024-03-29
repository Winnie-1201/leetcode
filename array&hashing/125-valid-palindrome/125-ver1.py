import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()

        start = 0
        end = len(s) - 1

        print(s)
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True

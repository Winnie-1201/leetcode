class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        left, right = 0, 0
        tMap = {}
        for c in t:
            tMap[c] = 1 if c not in tMap else 1 + tMap[c]
        sMap = {}
        res = s + t
        count = 0
        while right < len(s):
            char = s[right]
            if char in tMap:
                sMap[char] = 1 if char not in sMap else 1 + sMap[char]
                if sMap[char] == tMap[char]:
                    count += 1

            while count == len(tMap):
                lChar = s[left]
                temp = s[left: right + 1]
                if len(temp) < len(res):
                    res = temp
                if lChar in tMap:
                    sMap[lChar] -= 1
                    if sMap[lChar] < tMap[lChar]:
                        count -= 1
                left += 1
            right += 1

        return res if res != s + t else ""

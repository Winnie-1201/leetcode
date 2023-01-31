class Solution:
    def minWindow(self, s: str, t: str) -> str:

        left, right = 0, 0
        sMap = {}
        tSet = set(t)
        count = 0
        minStr = ""

        if len(t) <= 1 and t in s:
            return t

        while right < len(s):
            sMap[right] = s[right]

            if s[right] in tSet:
                count += 1
            right += 1

            if count >= len(t) and (len(sMap.values()) < len(minStr) or len(minStr) == 0):

                minStr = "".join(sMap.values())

            while left < len(s) and (count > len(t) - 1 or s[left] not in tSet):

                if s[left] in tSet:
                    count -= 1

                if left in sMap:
                    del sMap[left]
                left += 1

        return minStr


# solved it
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        left, right = 0, 0
        tMap = {}
        sMap = {}

        for i in t:
            tMap[i] = 1 + tMap.get(i, 0)

        temp = ""
        res = ""

        have, need = 0, len(tMap)
        while right < len(s):
            temp += s[right]

            if s[right] in tMap:
                sMap[s[right]] = 1 + sMap.get(s[right], 0)
                if sMap[s[right]] == tMap[s[right]]:
                    have += 1

            while have == need:
                if len(temp) < len(res) or len(res) == 0:
                    res = temp
                temp = temp[1:]

                if s[left] in sMap:
                    sMap[s[left]] -= 1
                    if sMap[s[left]] < tMap[s[left]]:
                        have -= 1
                left += 1
            right += 1

        return res

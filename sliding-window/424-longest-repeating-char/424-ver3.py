class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # does not work
        res = 1
        obj = {}
        left, right, temp = 0, 0, 0
        maxCount = 0
        while right < len(s):
            obj[s[right]] = 1 if s[right] not in obj else obj[s[right]] + 1
            maxCount = max(maxCount, obj[s[right]])
            # temp += 1
            while right - left - maxCount + 1 > k and left < right:
                print(right, left, maxCount)
                print(obj)
                obj[s[left]] -= 1
                temp -= 1
                res = max(res, temp)
                left += 1
                if obj[s[left]] == 0:
                    obj.remove(s[left])
            right += 1
        return res

# solution


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        obj = {}
        left, right = 0, 0
        maxCount = 0
        while right < len(s):
            obj[s[right]] = 1 if s[right] not in obj else obj[s[right]] + 1
            maxCount = max(maxCount, obj[s[right]])
            if right - left - maxCount + 1 > k:
                obj[s[left]] -= 1
                left += 1
            res = max(right - left + 1, res)
            right += 1
        return res

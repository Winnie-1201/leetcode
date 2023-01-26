class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # other method:
        # for idx in set(s):
        #     if s.count(idx) != t.count(idx): return False
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        # print(dic)
        for i in t:
            if not i in dic or dic[i] <= 0:
                return False
            elif i in dic:
                dic[i] -= 1

        return True

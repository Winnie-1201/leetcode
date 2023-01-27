from ast import List

# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging
# the letters of a different word or phrase, typically
# using all the original letters exactly once.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        obj = {}
        for s in strs:
            # print(obj, s)
            if obj and str("".join(sorted(s))) in obj and self.isAnagram(s, obj[str("".join(sorted(s)))][0]):
                obj[str("".join(sorted(s)))].append(s)
            else:
                obj[str("".join(sorted(s)))] = [s]
        # print(obj)

        return obj.values()

    def isAnagram(self, str1, str2):
        for i in set(str1):
            if str1.count(i) != str2.count(i):
                return False
        return True

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(s1))

        for i in range(len(s2) - len(s1)+1):
            if s1 == "".join(sorted(s2[i:len(s1)+i])):
                return True

        return False

#

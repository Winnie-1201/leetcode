from ast import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        obj = {}

        for i in range(len(s)):
            obj[s[i]] = i

        # print(obj)
        part = [0]
        far = [s[0], obj[s[0]]]
        for i in range(len(s)):
            # print(far, i)
            if obj[s[i]] == i and far[1] == i:
                part.append(i + 1 - sum(part))
                # far = [s[i + 1], obj[s[i + 1]]]
                if i < len(s) - 1:
                    far = [s[i + 1], obj[s[i + 1]]]

            if obj[s[i]] > far[1]:
                far = [s[i], obj[s[i]]]

        return part[1:]

        last = {c: i for i, c in enumerate(s)}
        curr = nxt = 0
        res = []

        for i, c in enumerate(s):
            curr = max(curr, last[c])

            if i == curr:
                res.append(i - nxt + 1)
                nxt = i + 1
        return res

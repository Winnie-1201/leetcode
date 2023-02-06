from ast import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        curr = temperatures[0]
        count = start = end = 0

        while end < len(temperatures):
            if temperatures[end] > curr:
                res.append(count)
                start += 1
                end = start + 1
                curr = temperatures[start]
                count = 1
            else:
                count += 1
                end += 1
                if end == len(temperatures) and start < len(temperatures):
                    res.append(0)
                    start += 1
                    curr = temperatures[start]
                    end = start + 1
                    count = 1

        res.append(0)

        return res

# time limit exceeded

# solution: Monotonic stack -> which means the list is in decresing order


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # element as pair: [temperature, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:

                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd

            stack.append([t, i])

            # ans = [0] * len(T)
            # stack = []
            # for i, t in enumerate(T):
            #   while stack and T[stack[-1]] < t:
            #     cur = stack.pop()
            #     ans[cur] = i - cur
            #   stack.append(i)

        return res

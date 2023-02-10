from ast import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carPair = []

        for i in range(len(position)):
            carPair.append([position[i], speed[i]])

        carPair.sort(reverse=True)
        stack = []

        for pair in carPair:
            stack.append(pair)

            if len(stack) >= 2 and (target - pair[0]) / pair[1] <= (target - stack[len(stack) - 2][0]) / stack[len(stack) - 2][1]:
                stack.pop()

        # list comprehension
        # carPair = [[p, s] for p, s in zip(position, speed)]

        # stack = []
        # for p, s in sorted(carPair)[::-1]: # sorted it in reverse order

        #     stack.append((target - p) / s)

        #     if len(stack) >= 2 and stack[-1] <= stack[-2]:
        #         stack.pop()

        return len(stack)

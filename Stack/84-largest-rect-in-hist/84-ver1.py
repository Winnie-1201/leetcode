from ast import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        idx = 0
        flag = False
        for i in range(len(heights)):

            while stack and heights[i] < stack[len(stack) - 1][1]:
                newArea = stack[len(stack) - 1][1] * \
                    (i - stack[len(stack) - 1][0])
                area = max(area, newArea)
                idx, h = stack.pop()
                flag = True

            # print(idx)
            if flag:
                stack.append([idx, heights[i]])
                flag = False
            else:
                stack.append([i, heights[i]])

            # while stack and heights[i] < stack[len(stack) - 1][1]:
            #     area = max(area, (i - stack[len(stack) - 1][0] + 1) * stack[len(stack) - 1][1])
            #     stack.pop()
            # stack.append([i, heights[i]])
            # area = max(len(stack) * min(stack), area)
            # while len(stack) >= 2 and (min(stack) * len(stack) < area or area < i):
            #     stack.popleft()
            # area = max(len(stack) * min(stack), area)
        # print(stack)
        for index, height in stack:
            newArea = (len(heights) - index) * height
            area = max(area, newArea)
        return area


# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         stack = []
#         area = 0
#         for i in range(len(heights)):
#             start = i
#             while stack and heights[i] < stack[len(stack) - 1][1]:
#                 index, height = stack.pop()
#                 area = max(area, height * (i - index))
#                 start = index
#             stack.append([start, heights[i]])
#         for index, height in stack:
#             newArea = (len(heights) - index) * height
#             area = max(area, newArea)
#         return area

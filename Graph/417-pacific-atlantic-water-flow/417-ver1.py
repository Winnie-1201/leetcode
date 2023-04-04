from ast import List
import collections


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Time Limit Exceeded
        # pacific: [0, i], [i, 0]
        # altantic: [i, len-1], [len-1, i]
        rows, cols = len(heights), len(heights[0])
        pacific, altantic = set(), set()

        for i in range(rows):
            pacific.add((i, 0))
            altantic.add((i, cols - 1))

        for i in range(cols):
            pacific.add((0, i))
            altantic.add((rows - 1, i))

        #
        def dfs(r, c):
            nei = collections.deque()
            visited = set()
            visited.add((r, c))
            nei.append((r, c))
            res = set()

            if (r, c) in pacific and (r, c) in altantic:
                res.add(0)
                res.add(1)
                return res
            if (r, c) in pacific:
                res.add(1)
            if (r, c) in altantic:
                res.add(0)

            while nei:
                r, c = nei.popleft()
                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if row in range(rows) and col in range(cols) and heights[row][col] <= heights[r][c] and (row, col) not in visited:

                        nei.append((row, col))
                        visited.add((row, col))
                        if (row, col) in pacific:
                            res.add(1)
                        if (row, col) in altantic:
                            res.add(0)

            return res

        result = []
        for r in range(rows):
            for c in range(cols):
                res = dfs(r, c)
                if len(res) == 2:
                    result.append([r, c])

        return result

from ast import List
import collections


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        areas = []

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            area = 1

            while q:
                r, c = q.popleft()
                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    # need new variables to store the updated row and col for each iteration
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1 and (row, col) not in visited:
                        visited.add((row, col))
                        q.append((row, col))
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    temp = bfs(r, c)
                    areas.append(temp)
                    maxArea = max(temp, maxArea)

        # print(areas)
        return maxArea

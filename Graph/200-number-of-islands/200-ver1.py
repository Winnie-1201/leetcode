from ast import List
import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                r, c = q.popleft()
                if r + 1 < rows and (r + 1, c) not in visited and grid[r+1][c] == "1":
                    visited.add((r+1, c))
                    q.append((r+1, c))
                if r - 1 >= 0 and (r - 1, c) not in visited and grid[r-1][c] == "1":
                    visited.add((r-1, c))
                    q.append((r-1, c))
                if c + 1 < cols and (r, c + 1) not in visited and grid[r][c+1] == "1":
                    visited.add((r, c + 1))
                    q.append((r, c + 1))

                if c - 1 >= 0 and (r, c - 1) not in visited and grid[r][c - 1] == "1":
                    visited.add((r, c - 1))
                    q.append((r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands

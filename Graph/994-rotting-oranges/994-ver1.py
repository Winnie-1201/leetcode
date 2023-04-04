from ast import List
import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # does not work some cases:
        # my solution only change its curr neighbor to rott at each iteration
        # in order to count the times of changing
        # but without traverse down enghou, it wont cover all of the cases
        visited = set()
        count = 0
        rows, cols = len(grid), len(grid[0])

#         def dfs(r, c, prev):
#             if (r, c) in visited or r == rows or c == cols or r < 0 or c < 0 or grid[r][c] == 0:
#                 return
#             if (r, c) not in visited and prev == 2:
#                 grid[r][c] = 2
#                 visited.add((r, c))

#             dfs(r + 1, c, grid[r][c])
#             dfs(r - 1, c, grid[r][c])
#             dfs(r, c + 1, grid[r][c])
#             dfs(r, c - 1, grid[r][c])

        def bfs(r, c):
            # if prev == 1 or prev == 0:
            #     return 0
            visited.add((r, c))
            change = 0
            drs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dr, dc in drs:
                row, col = r + dr, c + dc
                if row in range(rows) and col in range(cols) and grid[row][col] == 1 and grid[row][col] not in visited:
                    grid[row][col] = 2
                    visited.add((row, col))
                    change += 1
            return 0 if change == 0 else 1

        for r in range(rows):
            for c in range(cols):
                # dfs(r, c, grid[r][c])
                if grid[r][c] == 2:
                    count += bfs(r, c)
        print(grid)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        print(grid)
        return count


# my other solution wokrs:
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        count = 0
        rows, cols = len(grid), len(grid[0])
        rotted = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotted.append((r, c))

        while rotted:
            temp = collections.deque()
            while rotted:
                r, c = rotted.popleft()
                visited.add((r, c))
                drs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in drs:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1 and grid[row][col] not in visited:
                        grid[row][col] = 2
                        visited.add((row, col))
                        temp.append((row, col))
            rotted = temp
            count += 1

        print(grid)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return 0 if count == 0 else count - 1

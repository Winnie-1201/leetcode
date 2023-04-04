from ast import List
import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])
        rotted = collections.deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotted.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
                    
        while rotted and fresh > 0:
            for i in range(len(rotted)):
                r, c = rotted.popleft()
                drs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in drs:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                        grid[row][col] = 2
                        rotted.append((row, col))
                        fresh -= 1
            count += 1
                           
        return count if fresh == 0 else -1
                
        
                
        
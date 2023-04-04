from ast import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # a set: store the points with label
        # that can reach the border with label 0
        zero = set()
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (r, c) in zero or r == rows or c == cols or r < 0 or c < 0 or board[r][c] == "X":
                return
            zero.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if (r, c) not in zero and board[r][c] == "O":
                    board[r][c] = "X"

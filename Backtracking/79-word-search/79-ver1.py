from ast import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        path = set()

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if r < 0 or c < 0 or r >= ROW or c >= COL or word[idx] != board[r][c] or (r, c) in path:
                return False

            # add the visited point to path
            path.add((r, c))
            # check if the adjacent points are qualified
            res = dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx +
                                                1) or dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1)
            # after checking, needs to remove the point from the path
            path.remove((r, c))

            return res

        # check all of the points
        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0):
                    return True

        return False

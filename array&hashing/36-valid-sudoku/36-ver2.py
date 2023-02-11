from ast import List
import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in square[i//3, j//3]:
                    return False
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    square[i//3, j//3].add(board[i][j])

        return True

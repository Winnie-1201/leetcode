from ast import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(len(board)):
            newSet1 = set()
            # print(type(int(board[1][1])))
            for col in range(len(board[row])):
                if board[row][col] != "." and board[row][col] in newSet1:
                    return False
                else:
                    newSet1.add(board[row][col])

        # print("newset1", newSet1)
        for row in range(len(board)):
            newSet2 = set()
            for col in range(len(board[row])):
                if board[col][row] != "." and board[col][row] in newSet2:
                    return False
                else:
                    newSet2.add(board[col][row])

        # print("newset2", newSet2)
        hashset = {}
        for row in range(len(board)):
            for col in range(len(board[row])):
                # print(row//3, col//3, hashset, board[row][col])
                if (row//3, col//3) in hashset and board[row][col] != "." and board[row][col] in hashset[(row//3, col//3)]:
                    # print(row//3, col//3, hashset, board[row][col], )
                    return False
                elif (row//3, col//3) not in hashset:
                    hashset[(row//3, col//3)] = [board[row][col]]
                else:
                    hashset[(row//3, col//3)].append(board[row][col])

        # print(hashset)
        return True


# other solution
# class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     rows = collections.defaultdict(set)
    #     cols = collections.defaultdict(set)
    #     sqr = collections.defaultdict(set)

    #     for row in range(len(board)):
    #         for col in range(len(board[row])):
    #             if board[row][col] == ".":
    #                 continue
    #             if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in sqr[(row//3, col//3)]:
    #                 return False
    #             else:
    #                 rows[row].add(board[row][col])
    #                 cols[col].add(board[row][col])
    #                 sqr[(row//3, col//3)].add(board[row][col])
    #     return True

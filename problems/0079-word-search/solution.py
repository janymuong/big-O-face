"""
word search
https://leetcode.com/problems/word-search/
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, i: int) -> bool:
            # matched the whole word
            if i == len(word):
                return True

            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
                or board[r][c] != word[i]
            ):
                return False

            # mark this cell as "in use" for this path, then restore it
            # on the way back out (classic backtracking in-place trick)
            temp, board[r][c] = board[r][c], "#"

            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False


# if __name__ == "__main__":
#     sol = Solution()
#     board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
#     print(sol.exist(board, "ABCCED"))  # True
#     print(sol.exist(board, "SEE"))     # True
#     print(sol.exist(board, "ABCB"))    # False
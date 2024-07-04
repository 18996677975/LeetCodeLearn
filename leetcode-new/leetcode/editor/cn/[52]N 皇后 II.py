"""
N 皇后 II

# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。 
# 
#  
# 
#  
#  
#  示例 1： 
#  
#  
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#  
#  
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 9 
#  
# 
#  Related Topics回溯 
# 
#  👍 519, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.res = 0

    def totalNQueens(self, n: int) -> int:
        board = [["."] * n for _ in range(n)]
        self.backtrack(board, 0)
        return self.res

    def backtrack(self, board, row):
        n = len(board)

        if row == n:
            self.res += 1
            return

        for col in range(n):
            if not self.isVaild(board, row, col):
                continue
            board[row][col] = "Q"
            self.backtrack(board, row + 1)
            board[row][col] = "."

    def isVaild(self, board, row, col):
        n = len(board)

        for i in range(n):
            if board[row][i] == "Q":
                return False
            if board[i][col] == "Q":
                return False

        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1

        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        return True
# leetcode submit region end(Prohibit modification and deletion)

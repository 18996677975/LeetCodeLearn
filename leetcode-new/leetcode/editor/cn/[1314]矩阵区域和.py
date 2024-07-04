"""
矩阵区域和

# 给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 
# mat[r][c] 的和： 
# 
#  
#  i - k <= r <= i + k, 
#  j - k <= c <= j + k 且 
#  (r, c) 在矩阵内。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]
#  
# 
#  示例 2： 
# 
#  
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# 输出：[[45,45,45],[45,45,45],[45,45,45]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n, k <= 100 
#  1 <= mat[i][j] <= 100 
#  
# 
#  Related Topics数组 | 矩阵 | 前缀和 
# 
#  👍 199, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        numMatrix = NumMatrix(mat)
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # 左上角的坐标
                row1, col1 = max(i - k, 0), max(j - k, 0)
                # 右下角的坐标
                row2, col2 = min(i + k, m - 1), min(j + k, n - 1)

                res[i][j] = numMatrix.sumRegion(row1, col1, row2, col2)

        return res

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return

        self.preMatrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.preMatrix[i][j] = self.preMatrix[i][j - 1] + self.preMatrix[i - 1][j] + matrix[i - 1][j - 1] - \
                                           self.preMatrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preMatrix[row2 + 1][col2 + 1] - self.preMatrix[row1][col2 + 1] - self.preMatrix[row2 + 1][col1] + self.preMatrix[row1][col1]
# leetcode submit region end(Prohibit modification and deletion)

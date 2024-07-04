"""
螺旋矩阵

# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
#  
#  
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
# 
#  Related Topics数组 | 矩阵 | 模拟 
# 
#  👍 1702, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        upper_bound, right_bound, lower_bound, left_bound = 0, n - 1, m - 1, 0
        res = []

        # res.length == m * n 则遍历完整个数组
        while len(res) < m * n:
            # 在顶部从左向右遍历
            if upper_bound <= lower_bound:
                for j in range(left_bound, right_bound + 1):
                    res.append(matrix[upper_bound][j])
                # 上边界下移
                upper_bound += 1

            # 在右侧从上向下遍历
            if left_bound <= right_bound:
                for i in range(upper_bound, lower_bound + 1):
                    res.append(matrix[i][right_bound])
                # 右边界左移
                right_bound -= 1

            # 在底部从右向左遍历
            if upper_bound <= lower_bound:
                for j in range(right_bound, left_bound - 1, -1):
                    res.append(matrix[lower_bound][j])
                # 下边界上移
                lower_bound -= 1

            # 在左侧从下向上遍历
            if left_bound <= right_bound:
                for i in range(lower_bound, upper_bound - 1, -1):
                    res.append(matrix[i][left_bound])
                # 左边界右移
                left_bound += 1

        return res

# leetcode submit region end(Prohibit modification and deletion)

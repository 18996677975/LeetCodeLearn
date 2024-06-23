"""
螺旋矩阵 II

# 给你一个正整数 n ，生成一个包含 1 到 n² 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  
# 
#  Related Topics数组 | 矩阵 | 模拟 
# 
#  👍 1292, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        upper_bound, right_bound, lower_bound, left_bound = 0, n - 1, n - 1, 0
        res = [[0 for _ in range(n)] for _ in range(n)]
        # 需要填入矩阵的数字
        num = 1

        # 添如数字达到 n^2 停止
        while num <= n * n:
            # 顶部从左往右遍历
            if upper_bound <= lower_bound:
                for j in range(left_bound, right_bound + 1):
                    res[upper_bound][j] = num
                    num += 1
                # 上边界下移
                upper_bound += 1

            # 右侧从上往下遍历
            if left_bound <= right_bound:
                for i in range(upper_bound, lower_bound + 1):
                    res[i][right_bound] = num
                    num += 1
                # 右边界左移
                right_bound -= 1

            # 底部从右往左遍历
            if upper_bound <= lower_bound:
                for j in range(right_bound, left_bound - 1, -1):
                    res[lower_bound][j] = num
                    num += 1
                # 下边界上移
                lower_bound -= 1

            # 左侧从下往上遍历
            if left_bound <= right_bound:
                for i in range(lower_bound, upper_bound - 1, -1):
                    res[i][left_bound] = num
                    num += 1
                # 左边界右移
                left_bound += 1

        return res
# leetcode submit region end(Prohibit modification and deletion)

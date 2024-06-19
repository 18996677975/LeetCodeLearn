"""
# 给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 0
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 1
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 5 * 10⁶ 
#  
# 
#  Related Topics数组 | 数学 | 枚举 | 数论 
# 
#  👍 1167, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrimes = [True] * n

        for i in range(2, int(n ** 0.5) + 1):
            if isPrimes[i]:
                for j in range(i * i, n, i):
                    isPrimes[j] = False

        count = 0
        for i in range(2, n):
            if isPrimes[i]:
                count += 1

        return count
# leetcode submit region end(Prohibit modification and deletion)

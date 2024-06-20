"""
# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。 
# 
#  丑数 就是质因子只包含 2、3 和 5 的正整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 1690 
#  
# 
#  Related Topics哈希表 | 数学 | 动态规划 | 堆（优先队列） 
# 
#  👍 1188, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5 = 1, 1, 1
        product2, product3, product5 = 1, 1, 1
        p = 1

        ugly = [0] * (n + 1)

        while p <= n:
            minv = min(product2, product3, product5)
            ugly[p] = minv
            p += 1

            if minv == product2:
                product2 = ugly[p2] * 2
                p2 += 1
            if minv == product3:
                product3 = ugly[p3] * 3
                p3 += 1
            if minv == product5:
                product5 = ugly[p5] * 5
                p5 += 1

        return ugly[n]

# leetcode submit region end(Prohibit modification and deletion)

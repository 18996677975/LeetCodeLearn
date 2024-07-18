"""
不同的二叉搜索树

# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：n = 3
# 输出：5
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
#  1 <= n <= 19 
#  
# 
#  Related Topics树 | 二叉搜索树 | 数学 | 动态规划 | 二叉树 
# 
#  👍 2518, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        # 备忘录
        self.memo = []

    def numTrees(self, n: int) -> int:
        self.memo = [[0 for i in range(n + 1)] for j in range(n + 1)]
        # 计算闭区间 [1, n] 组成的 BST 个数
        return self.count(1, n)

    # 计算闭区间 [lo, hi] 组成的 BST 个数
    def count(self, lo: int, hi: int):
        if lo > hi:
            return 1

        # 查备忘录
        if self.memo[lo][hi] != 0:
            return self.memo[lo][hi]

        res = 0
        for i in range(lo, hi + 1):
            # i 的值作为根节点 root
            left = self.count(lo, i - 1)
            right = self.count(i + 1, hi)
            # 左右子树的组合数乘积是 BST 的总数
            res += left * right
        self.memo[lo][hi] = res

        return res
# leetcode submit region end(Prohibit modification and deletion)

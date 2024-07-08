"""
零钱兑换

# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。 
# 
#  计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。 
# 
#  你可以认为每种硬币的数量是无限的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1 
# 
#  示例 2： 
# 
#  
# 输入：coins = [2], amount = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：coins = [1], amount = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 2³¹ - 1 
#  0 <= amount <= 10⁴ 
#  
# 
#  Related Topics广度优先搜索 | 数组 | 动态规划 
# 
#  👍 2837, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 数组大小为 amount+1，初始值也为 amount+1
        dp = [(amount + 1) for _ in range(amount + 1)]
        # base case
        # 初始值为0
        dp[0] = 0

        # 外层 for 循环在遍历所有状态的所有取值
        for i in range(1, amount + 1):
            # 内层 for 循环在求所有选择的最小值
            for coin in coins:
                # 子问题无解，跳过
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # 如果结果是初始值，则表示没有找到解
        return dp[amount] if dp[amount] != (amount + 1) else -1
# leetcode submit region end(Prohibit modification and deletion)

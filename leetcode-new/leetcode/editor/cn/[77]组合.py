"""
组合

# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。 
# 
#  你可以按 任何顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
# 
#  示例 2： 
# 
#  
# 输入：n = 1, k = 1
# 输出：[[1]] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  
# 
#  Related Topics回溯 
# 
#  👍 1635, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [_ for _ in range(1, n + 1)]
        self.backtrack(nums, [], 0, k)
        return self.res

    def backtrack(self, nums: List[int], track: List[int], start, k):
        # base case
        if len(track) == k:
            # 遍历到了第 k 层，收集当前节点的值
            self.res.append(track.copy())
            return

        # 回溯算法标准框架
        for i in range(start, len(nums)):
            # 做选择
            track.append(nums[i])
            # 通过 start 参数控制树枝的遍历，避免产生重复的子集
            self.backtrack(nums, track, i + 1, k)
            # 撤销选择
            track.pop()
# leetcode submit region end(Prohibit modification and deletion)

"""
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的 子集（幂集）。 
# 
#  解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。 
# 
#  
#  
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  
# 
#  Related Topics位运算 | 数组 | 回溯 
# 
#  👍 1217, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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
        self.track = []
        self.vaild = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.vaild = [False for _ in range(len(nums))]
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], start: int):
        self.res.append(self.track.copy())

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1] and not self.vaild[i]:
                continue
            self.track.append(nums[i])
            self.vaild[i] = True
            self.backtrack(nums, i + 1)
            self.track.pop()
            self.vaild[i] = False
# leetcode submit region end(Prohibit modification and deletion)

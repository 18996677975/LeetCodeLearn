"""
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
# 
#  Related Topics数组 | 回溯 
# 
#  👍 1580, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.res = []    # 用于存储结果
        self.track = []  # 用于存储路径
        self.vaild = []  # 记录元素是否使用过

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 先排序，让相同的元素靠在一起
        nums.sort()
        self.vaild = [False for _ in range(len(nums))]
        self.backtrack(nums)
        return self.res

    def backtrack(self, nums: List[int]):
        if len(self.track) == len(nums):
            self.res.append(self.track.copy())
            return

        for i in range(len(nums)):
            if self.vaild[i]:
                continue
            # 新添加的剪枝逻辑，固定相同的元素在排列中的相对位置
            if i > 0 and nums[i] == nums[i - 1] and not self.vaild[i - 1]:
                continue
            self.track.append(nums[i])
            self.vaild[i] = True
            self.backtrack(nums)
            self.track.pop()
            self.vaild[i] = False
# leetcode submit region end(Prohibit modification and deletion)

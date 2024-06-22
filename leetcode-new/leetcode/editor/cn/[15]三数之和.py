"""
三数之和

# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != 
# k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请 
# 
#  你返回所有和为 0 且不重复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
# 
#  Related Topics数组 | 双指针 | 排序 
# 
#  👍 6906, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSumTarget(self, nums: List[int], target: int, start: int) -> List[List[int]]:
        lo, hi = start, len(nums) - 1
        res = []
        while lo < hi:
            s = nums[lo] + nums[hi]
            left, right = nums[lo], nums[hi]
            if s < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
            elif s > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1
            elif s == target:
                res.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return res

    def threeSumTarget(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        i = 0
        while i < n:
            tuples = self.twoSumTarget(nums, target - nums[i], i + 1)
            for t in tuples:
                t.append(nums[i])
                res.append(t)
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            else:
                i += 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums 必须有序
        nums.sort()
        return self.threeSumTarget(nums, 0)
# leetcode submit region end(Prohibit modification and deletion)

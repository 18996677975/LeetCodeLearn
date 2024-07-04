"""
四数之和

# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[
# b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）： 
# 
#  
#  0 <= a, b, c, d < n 
#  a、b、c 和 d 互不相同 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  你可以按 任意顺序 返回答案 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  Related Topics数组 | 双指针 | 排序 
# 
#  👍 1924, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
"""
1、沿用 三数之和 
"""
# class Solution:
#     def twoSumTarget(self, nums: List[int], target: int, start: int) -> List[List[int]]:
#         lo, hi = start, len(nums) - 1
#         res = []
#         while lo < hi:
#             s = nums[lo] + nums[hi]
#             left, right = nums[lo], nums[hi]
#             if s < target:
#                 while lo < hi and nums[lo] == left:
#                     lo += 1
#             elif s > target:
#                 while lo < hi and nums[hi] == right:
#                     hi -= 1
#             elif s == target:
#                 res.append([left, right])
#                 while lo < hi and nums[lo] == left:
#                     lo += 1
#                 while lo < hi and nums[hi] == right:
#                     hi -= 1
#         return res
#
#     def threeSumTarget(self, nums: List[int], target: int, start: int) -> List[List[int]]:
#         n = len(nums)
#         res = []
#         i = start
#         while i < n:
#             tuples = self.twoSumTarget(nums, target - nums[i], i + 1)
#             for t in tuples:
#                 t.append(nums[i])
#                 res.append(t)
#             while i < n - 1 and nums[i] == nums[i + 1]:
#                 i += 1
#             else:
#                 i += 1
#         return res
#
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums.sort()
#         n = len(nums)
#         res = []
#         i = 0
#         while i < n:
#             triples = self.threeSumTarget(nums, target - nums[i], i + 1)
#             for triple in triples:
#                 triple.append(nums[i])
#                 res.append(triple)
#             while i < n - 1 and nums[i] == nums[i + 1]:
#                 i += 1
#             else:
#                 i += 1
#
#         return res

"""
2、统一方式 nSum
"""
class Solution:
    def nSum(self, nums: List[int], n: int, start: int, target: int):
        sz = len(nums)
        res = []
        # 至少是 2Sum，且数组大小不应该小于 n
        if n < 2 or sz < n:
            return res

        # 2Sum 是 base case
        if n == 2:
            lo, hi = start, sz - 1
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
        else:
            # n > 2 时，递归计算 (n-1)Sum 的结果
            idx = start
            while idx < sz:
                sub = self.nSum(nums, n - 1, idx + 1, target - nums[idx])
                for arr in sub:
                    # (n-1)Sum 加上 nums[i] 就是 nSum
                    arr.append(nums[idx])
                    res.append(arr)
                # idx 前进
                while idx < sz - 1 and nums[idx] == nums[idx + 1]:
                    idx += 1
                else:
                    idx += 1

        return res


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.nSum(nums, 4, 0, target)
# leetcode submit region end(Prohibit modification and deletion)

"""
除自身以外数组的乘积

# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。 
# 
#  题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内。 
# 
#  请 不要使用除法，且在 O(n) 时间复杂度内完成此题。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 10⁵ 
#  -30 <= nums[i] <= 30 
#  保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内 
#  
# 
#  
# 
#  进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。） 
# 
#  Related Topics数组 | 前缀和 
# 
#  👍 1801, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # 从左到右的前缀积，prefix[i] 是 nums[0..i] 的元素积
        prefix = [1] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
        # print(prefix)

        # 从右到左的前缀积，suffix[i] 是 nums[i..n-1] 的元素积
        suffix = [1] * n
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        # print(suffix)

        # 结果数组
        res = [0] * n
        res[0] = suffix[1]
        res[n - 1] = prefix[n - 2]

        for i in range(1, n - 1):
            # print("prefix: " + str(prefix[i - 1]) + "\tsuffix: " + str(suffix[i + 1]))
            res[i] = prefix[i - 1] * suffix[i + 1]

        return res
# leetcode submit region end(Prohibit modification and deletion)

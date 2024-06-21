"""
# 给你一个已经 排好序 的整数数组 nums 和整数 a 、 b 、 c 。对于数组中的每一个元素 nums[i] ，计算函数值 f(x) = ax² + 
# bx + c ，请 按升序返回数组 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# 输出: [3,9,15,33]
#  
# 
#  示例 2： 
# 
#  
# 输入: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# 输出: [-23,-5,1,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  -100 <= nums[i], a, b, c <= 100 
#  nums 按照 升序排列 
#  
# 
#  
# 
#  进阶：你可以在时间复杂度为 O(n) 的情况下解决这个问题吗？ 
# 
#  Related Topics数组 | 数学 | 双指针 | 排序 
# 
#  👍 77, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        i, j = 0, len(nums) - 1
        p = len(nums) - 1 if a > 0 else 0

        res = [0 for _ in range(len(nums))]

        while i <= j:
            v1, v2 = self.f(nums[i], a, b, c), self.f(nums[j], a, b, c)

            if a > 0:
                if v1 > v2:
                    res[p] = v1
                    i += 1
                else:
                    res[p] = v2
                    j -= 1
                p -= 1
            else:
                if v1 > v2:
                    res[p] = v2
                    j -= 1
                else:
                    res[p] = v1
                    i += 1
                p += 1

        return res

    def f(self, x, a, b, c):
        return a * x * x + b * x + c
# leetcode submit region end(Prohibit modification and deletion)

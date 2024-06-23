"""
将 x 减到 0 的最小操作数

# 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改
#  数组以供接下来的操作使用。 
# 
#  如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,4,2,3], x = 5
# 输出：2
# 解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,6,7,8,9], x = 4
# 输出：-1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,2,20,1,1,3], x = 10
# 输出：5
# 解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁴ 
#  1 <= x <= 10⁹ 
#  
# 
#  Related Topics数组 | 哈希表 | 二分查找 | 前缀和 | 滑动窗口 
# 
#  👍 353, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        # 求数组总和
        num_sum = sum(nums)
        # 滑动窗口需要寻找的子数组目标和
        target = num_sum - x

        left, right = 0, 0
        # 记录目标子数组的最大长度
        res = -1
        # 记录窗口内所有元素和
        window_sum = 0

        while right < n:
            # 扩大窗口
            window_sum += nums[right]
            right += 1

            while left < right and window_sum > target:
                # 缩小窗口
                d = nums[left]
                window_sum -= d
                left += 1

            # 寻找目标子数组
            if window_sum == target:
                res = max(res, right - left)

        # 目标子数组的最大长度可以推导出需要删除的字符数量
        return -1 if res == -1 else (n - res)
# leetcode submit region end(Prohibit modification and deletion)

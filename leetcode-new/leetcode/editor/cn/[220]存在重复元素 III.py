"""
存在重复元素 III

# 给你一个整数数组 nums 和两个整数 indexDiff 和 valueDiff 。 
# 
#  找出满足下述条件的下标对 (i, j)： 
# 
#  
#  i != j, 
#  abs(i - j) <= indexDiff 
#  abs(nums[i] - nums[j]) <= valueDiff 
#  
# 
#  如果存在，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
# 输出：true
# 解释：可以找出 (i, j) = (0, 3) 。
# 满足下述 3 个条件：
# i != j --> 0 != 3
# abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
# abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
# 输出：false
# 解释：尝试所有可能的下标对 (i, j) ，均无法满足这 3 个条件，因此返回 false 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  1 <= indexDiff <= nums.length 
#  0 <= valueDiff <= 10⁹ 
#  
# 
#  Related Topics数组 | 桶排序 | 有序集合 | 排序 | 滑动窗口 
# 
#  👍 733, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *
import bisect

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        from sortedcontainers import SortedSet
        n = len(nums)
        left, right = 0, 0
        window = SortedSet()

        # 滑动窗口算法框架，维护一个大小为 k 的窗口
        while right < n:
            # 当窗口的大小大于 k 时，缩小窗口
            if (right - left) > indexDiff:
                window.remove(nums[left])
                left += 1

            index = bisect.bisect_left(window, nums[right] - valueDiff)
            if window and 0 <= index < len(window) and abs(window[index] - nums[right]) <= valueDiff:
                return True

            window.add(nums[right])
            right += 1

        return False
# leetcode submit region end(Prohibit modification and deletion)

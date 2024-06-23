"""
最大连续1的个数 III

# 给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释：[1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  nums[i] 不是 0 就是 1 
#  0 <= k <= nums.length 
#  
# 
#  Related Topics数组 | 二分查找 | 前缀和 | 滑动窗口 
# 
#  👍 705, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, 0
        # 记录窗口中 1 的出现次数
        window_all_one = 0
        # 记录结果长度
        res = 0

        # 开始滑动窗口模板
        while right < n:
            # 扩大窗口
            # 当 nums[right] 为 1 时 window_all_one 直接加1，否则在 window_all_one 加 1 基础上还需要将 k 减 1 （可变次数减 1 ）
            if nums[right] == 1:
                window_all_one += 1
            else:
                window_all_one += 1
                k -= 1
            right += 1

            # 当可变次数小于 0 时，缩小窗口
            while left < right and k < 0:
                # 遇到 nums[left] 为 0 时，k 加 1
                if nums[left] == 0:
                    k += 1
                window_all_one -= 1
                left += 1

            # 此时一定是一个合法的窗口，求最大窗口长度
            res = max(res, window_all_one)

        return res
# leetcode submit region end(Prohibit modification and deletion)

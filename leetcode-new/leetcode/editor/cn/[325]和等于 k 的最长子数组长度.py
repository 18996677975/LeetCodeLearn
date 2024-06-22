"""
和等于 k 的最长子数组长度

# 给定一个数组 nums 和一个目标值 k，找到和等于 k 的最长连续子数组长度。如果不存在任意一个符合要求的子数组，则返回 0。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,-1,5,-2,3], k = 3
# 输出: 4 
# 解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [-2,-1,2,1], k = 1
# 输出: 2 
# 解释: 子数组 [-1, 2] 和等于 1，且长度最长。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  -10⁹ <= k <= 10⁹ 
#  
# 
#  Related Topics数组 | 哈希表 | 前缀和 
# 
#  👍 234, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)

        preSum = [0] * (n + 1)
        valToIndex = {0: 0}
        res = 0

        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
            need = preSum[i] - k
            if need in valToIndex:
                res = max(res, i - valToIndex[need])
            if preSum[i] not in valToIndex:
                valToIndex[preSum[i]] = i

        return res
# leetcode submit region end(Prohibit modification and deletion)

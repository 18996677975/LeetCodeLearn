"""
和可被 K 整除的子数组

# 给定一个整数数组 nums 和一个整数 k ，返回其中元素之和可被 k 整除的非空 子数组 的数目。 
# 
#  子数组 是数组中 连续 的部分。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [4,5,0,-2,-3,1], k = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 k = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [5], k = 9
# 输出: 0
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  2 <= k <= 10⁴ 
#  
# 
#  Related Topics数组 | 哈希表 | 前缀和 
# 
#  👍 511, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # nums 的前缀和数组，注意索引偏移，preSum[i] 的值为 sum(nums[0..i-1])
        preSum = [0] * (n + 1)
        # 前缀和余数的计数器，方便快速查找所需的前缀和余数的数量
        remainderToCount = {0: 1}
        # 计算 nums 的前缀和余数并更新计数器
        res = 0

        for i in range(1, n + 1):
            # 计算 nums[0..i] 的前缀和
            preSum[i] = preSum[i - 1] + nums[i - 1]
            # nums[0..i] 的所有元素之和与 k 的余数
            curRemainder = preSum[i] % k
            # Python 求模的特性，-2 % 3 = 1，但我们实际想要正余数 -2
            if curRemainder < 0:
                curRemainder = curRemainder + k

            # 看看之前 nums[0..i-1] 中是否也存在前缀和余数为 curRemainder 的子数组
            if curRemainder in remainderToCount:
                # 如果存在，则说明找到了可以整除 k 的子数组，累加子数组数量
                count = remainderToCount.get(curRemainder)
                res += count
                remainderToCount[curRemainder] = count + 1
            else:
                # 如果不存在，那么 nums[0..i] 是第一个前缀和余数为 curRemainder 的子数组
                remainderToCount[curRemainder] = 1

        return res
# leetcode submit region end(Prohibit modification and deletion)

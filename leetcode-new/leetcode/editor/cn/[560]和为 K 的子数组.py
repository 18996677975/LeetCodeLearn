"""
和为 K 的子数组

# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。 
# 
#  子数组是数组中元素的连续非空序列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1], k = 2
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3], k = 3
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -1000 <= nums[i] <= 1000 
#  -10⁷ <= k <= 10⁷ 
#  
# 
#  Related Topics数组 | 哈希表 | 前缀和 
# 
#  👍 2386, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # 前缀和数组
        preSum = [0] * (n + 1)
        # 前缀和到该前缀和出现次数的映射，方便快速查找所需的前缀和
        count = {0: 1}
        res = 0

        # 计算 nums 的前缀和
        for i in range(1, len(preSum)):
            preSum[i] = preSum[i - 1] + nums[i - 1]
            # 如果之前存在值为 need 的前缀和
            # 说明存在以 nums[i-1] 结尾的子数组的和为 k ( preSum[i] - need = k )
            need = preSum[i] - k
            if need in count:
                res += count.get(need)

            # 将当前前缀和存入哈希表
            if preSum[i] not in count:
                count[preSum[i]] = 1
            else:
                count[preSum[i]] += 1

        return res
# leetcode submit region end(Prohibit modification and deletion)

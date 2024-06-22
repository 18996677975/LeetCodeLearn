"""
表现良好的最长时间段

# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。 
# 
#  我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。 
# 
#  所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。 
# 
#  请你返回「表现良好时间段」的最大长度。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。 
# 
#  示例 2： 
# 
#  
# 输入：hours = [6,6,6]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= hours.length <= 10⁴ 
#  0 <= hours[i] <= 16 
#  
# 
#  Related Topics栈 | 数组 | 哈希表 | 前缀和 | 单调栈 
# 
#  👍 536, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        preSum = [0] * (n + 1)
        # 前缀和到索引的映射，方便快速查找所需的前缀和
        valToIndex = {}
        res = 0

        for i in range(1, n + 1):
            # 计算 hours[0..i-1] 的前缀和
            preSum[i] = preSum[i - 1] + (1 if hours[i - 1] > 8 else -1)
            # 如果这个前缀和还没有对应的索引，说明这个前缀和第一次出现，记录下来
            # 因为题目想找长度最大的子数组，valToIndex 中的索引应尽可能小，因此如果 preSum[i] in valToIndex 时什么都不做
            if preSum[i] not in valToIndex:
                valToIndex[preSum[i]] = i

            # 现在我们想找 hours[0..i-1] 中元素和大于 0 的子数组，根据 preSum[i] 的正负分情况讨论了
            # preSum[i] 为正，说明 hours[0..i-1] 都是「表现良好的时间段」
            if preSum[i] > 0:
                res = max(res, i)
            # preSum[i] 为负，需要寻找一个 j 使得 preSum[i] - preSum[j] > 0
            # 且 j 应该尽可能小，即寻找 preSum[j] == preSum[i] - 1 ==> preSum[i] - preSum[j] = 1
            else:
                if (preSum[i] - 1) in valToIndex:
                    j = valToIndex.get(preSum[i] - 1)
                    res = max(res, i - j)

        return res
# leetcode submit region end(Prohibit modification and deletion)

"""
查找和最小的 K 对数字

# 给定两个以 非递减顺序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。 
# 
#  定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。 
# 
#  请找到和最小的 k 个数对 (u1,v1), (u2,v2) ... (uk,vk) 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
#      [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
#      [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums1.length, nums2.length <= 10⁵ 
#  -10⁹ <= nums1[i], nums2[i] <= 10⁹ 
#  nums1 和 nums2 均为 升序排列 
#  
#  1 <= k <= 10⁴ 
#  k <= nums1.length * nums2.length 
#  
# 
#  Related Topics数组 | 堆（优先队列） 
# 
#  👍 597, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""
import heapq
from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(nums1)):
            heapq.heappush(heap, [nums1[i] + nums2[0], nums1[i], nums2[0], 0])

        res = []

        while len(heap) > 0 and k > 0:
            _, num1, num2, idx = heapq.heappop(heap)
            k -= 1

            next_idx = idx + 1

            if next_idx < len(nums2):
                heapq.heappush(heap, [num1 + nums2[next_idx], num1, nums2[next_idx], next_idx])

            res.append([num1, num2])

        return res
# leetcode submit region end(Prohibit modification and deletion)

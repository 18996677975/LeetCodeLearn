"""
拼车

# 车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向） 
# 
#  给定整数 capacity 和一个数组 trips , trip[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有
#  numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。 
# 
#  当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 4
# 输出：false
#  
# 
#  示例 2： 
# 
#  
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 5
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= trips.length <= 1000 
#  trips[i].length == 3 
#  1 <= numPassengersi <= 100 
#  0 <= fromi < toi <= 1000 
#  1 <= capacity <= 10⁵ 
#  
# 
#  Related Topics数组 | 前缀和 | 排序 | 模拟 | 堆（优先队列） 
# 
#  👍 384, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Difference:
    # 差分数组
    def __init__(self, nums: List[int]):
        assert len(nums) > 0
        self.diff = [0] * len(nums)
        # 根据初始数组构造差分数组
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]

    # 给闭区间 [i, j] 增加 val（可以是负数）
    def increment(self, i: int, j: int, val: int) -> None:
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    # 返回结果数组
    def result(self) -> List[int]:
        res = [0] * len(self.diff)
        # 根据差分数组构造结果数组
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
        return res

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nums = [0] * 1001
        df = Difference(nums)

        for trip in trips:
            i, j, val = trip[1], trip[2] - 1, trip[0]
            df.increment(i, j, val)

        res = df.result()

        for i in range(len(res)):
            if res[i] > capacity:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)

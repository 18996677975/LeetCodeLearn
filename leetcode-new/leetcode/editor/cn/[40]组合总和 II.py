"""
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用 一次 。 
# 
#  注意：解集不能包含重复的组合。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ] 
# 
#  示例 2: 
# 
#  
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ] 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
# 
#  Related Topics数组 | 回溯 
# 
#  👍 1559, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.vaild = []
        self.trackSum = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.vaild = [False for _ in range(len(candidates))]
        self.backtrack(candidates, target, 0)
        return self.res

    def backtrack(self, candidates: List[int], target: int, start: int):
        if self.trackSum == target:
            self.res.append(self.track.copy())
        if self.trackSum > target:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1] and not self.vaild[i]:
                continue
            self.track.append(candidates[i])
            self.trackSum += candidates[i]
            self.vaild[i] = True
            self.backtrack(candidates, target, i + 1)
            self.track.pop()
            self.trackSum -= candidates[i]
            self.vaild[i] = False
# leetcode submit region end(Prohibit modification and deletion)

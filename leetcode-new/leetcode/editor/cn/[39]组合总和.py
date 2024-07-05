"""
# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的
#  所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。 
# 
#  candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
# 
#  对于给定的输入，保证和为 target 的不同组合数少于 150 个。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。 
# 
#  示例 2： 
# 
#  
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]] 
# 
#  示例 3： 
# 
#  
# 输入: candidates = [2], target = 1
# 输出: []
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= candidates.length <= 30 
#  2 <= candidates[i] <= 40 
#  candidates 的所有元素 互不相同 
#  1 <= target <= 40 
#  
# 
#  Related Topics数组 | 回溯 
# 
#  👍 2832, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        # 记录结果
        self.res = []
        # 记录回溯的路径
        self.track = []
        # 记录 track 中的路径和
        self.trackSum = 0

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtrack(candidates, target, 0)
        return self.res

    def backtrack(self, candidates: List[int], target: int, start: int):
        # base case，找到目标和，记录结果
        if self.trackSum == target:
            self.res.append(self.track.copy())
            return
        # base case，超过目标和，停止向下遍历
        if self.trackSum > target:
            return
        # 回溯算法标准框架
        for i in range(start, len(candidates)):
            # 选择 candidates[i]
            self.track.append(candidates[i])
            self.trackSum += candidates[i]
            # 递归遍历下一层回溯树
            # 同一元素可重复使用，注意参数
            self.backtrack(candidates, target, i)
            # 撤销选择 candidates[i]
            self.track.pop()
            self.trackSum -= candidates[i]
# leetcode submit region end(Prohibit modification and deletion)

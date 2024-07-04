"""
全排列

# 给定一个不含重复数字的整数数组 nums ，返回其 所有可能的全排列 。可以 按任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  nums 中的所有整数 互不相同 
#  
# 
#  
# 
#  
#  注意：本题与主站 46 题相同：https://leetcode-cn.com/problems/permutations/ 
# 
#  Related Topics数组 | 回溯 
# 
#  👍 81, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def __init__(self):
    #     self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(state=[], choices=nums, selected=[False] * len(nums), res=res)
        return res

    def backtrack(self, state, choices, selected, res):
        if len(state) == len(choices):
            res.append(list(state))
            return
        for i, choice in enumerate(choices):
            # 剪枝：不允许重复选择元素
            if not selected[i]:
                # 尝试：做出选择，更新状态
                selected[i] = True
                state.append(choice)
                # 进行下一轮选择
                self.backtrack(state, choices, selected, res)
                # 回退：撤销选择，恢复到之前的状态
                selected[i] = False
                state.pop()
# leetcode submit region end(Prohibit modification and deletion)

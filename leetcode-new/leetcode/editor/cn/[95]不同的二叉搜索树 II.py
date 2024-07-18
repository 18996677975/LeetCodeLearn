"""
不同的二叉搜索树 II

# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。 
# 
#  
# 
#  
#  
#  示例 1： 
#  
#  
# 输入：n = 3
# 输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
#  
#  
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
# 
#  Related Topics树 | 二叉搜索树 | 动态规划 | 回溯 | 二叉树 
# 
#  👍 1562, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        # 构造闭区间 [1, n] 组成的 BST
        return self.build(1, n)

    # 计算闭区间 [lo, hi] 组成的 BST 个数
    def build(self, lo: int, hi: int):
        res = []

        if lo > hi:
            res.append(None)
            return res

        # 1、穷举 root 节点的所有可能。
        for i in range(lo, hi + 1):
            # 2、递归构造出左右子树的所有有效 BST。
            leftTree = self.build(lo, i - 1)
            rightTree = self.build(i + 1, hi)
            # 3、给 root 节点穷举所有左右子树的组合。
            for left in leftTree:
                for right in rightTree:
                    # i 作为根节点 root 的值
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)

        return res
# leetcode submit region end(Prohibit modification and deletion)

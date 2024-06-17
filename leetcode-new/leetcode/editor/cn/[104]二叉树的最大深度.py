"""
二叉树的最大深度

# 给定一个二叉树 root ，返回其最大深度。 
# 
#  二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1,null,2]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数量在 [0, 10⁴] 区间内。 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics树 | 深度优先搜索 | 广度优先搜索 | 二叉树 
# 
#  👍 1836, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
1、遍历的方式
"""
class Solution:
    def __init__(self):
        self.depth = 0
        self.res = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return

        # 前序遍历位置
        self.depth += 1
        # 到叶子节点时进行 res 最大值判断
        if not root.left and not root.right:
            self.res = max(self.res, self.depth)

        self.traverse(root.left)
        self.traverse(root.right)
        # 后序遍历位置
        self.depth -= 1

"""
2、分解的方式
"""
class Solution:
    # 定义：输入根节点，返回这棵二叉树的最大深度
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return max(leftDepth, rightDepth) + 1
# leetcode submit region end(Prohibit modification and deletion)

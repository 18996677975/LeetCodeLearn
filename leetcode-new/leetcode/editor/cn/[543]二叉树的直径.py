"""
二叉树的直径

# 给你一棵二叉树的根节点，返回该树的 直径 。 
# 
#  二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。 
# 
#  两节点之间路径的 长度 由它们之间边数表示。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3,4,5]
# 输出：3
# 解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1,2]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [1, 10⁴] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics树 | 深度优先搜索 | 二叉树 
# 
#  👍 1550, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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
该方式在本题中会超时，遍历前序方式无法获取到子树的数据，必须重复查询子树深度，导致时间复杂度为 O(n**2)
"""
# class Solution:
#     def __init__(self):
#         self.maxDiaMeter = 0
#
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         self.traverse(root)
#         return self.maxDiaMeter
#
#     def traverse(self, root):
#         if not root:
#             return 0
#
#         leftDepth = self.maxDepth(root.left)
#         rightDepth = self.maxDepth(root.right)
#
#         myDiaMeter = leftDepth + rightDepth
#
#         self.maxDiaMeter = max(myDiaMeter, self.maxDiaMeter)
#
#         self.traverse(root.left)
#         self.traverse(root.right)
#
#     def maxDepth(self, root):
#         if not root:
#             return 0
#
#         leftDepth = self.maxDepth(root.left)
#         rightDepth = self.maxDepth(root.right)
#
#         return max(leftDepth, rightDepth) + 1

"""
2、分解的方式
"""
class Solution:
    def __init__(self):
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.maxDiameter

    def maxDepth(self, root):
        if not root:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        self.maxDiameter = max(self.maxDiameter, leftDepth + rightDepth)

        return max(leftDepth, rightDepth) + 1
# leetcode submit region end(Prohibit modification and deletion)

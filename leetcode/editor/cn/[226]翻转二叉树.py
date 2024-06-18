"""
# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root = [2,1,3]
# 输出：[2,3,1]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目范围在 [0, 100] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics树 | 深度优先搜索 | 广度优先搜索 | 二叉树 
# 
#  👍 1818, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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
遍历的方式
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root

    def traverse(self, root):
        if not root:
            return

        leftNode, rightNode = root.left, root.right
        root.left = rightNode
        root.right = leftNode

        self.traverse(root.left)
        self.traverse(root.right)

"""
分解问题的方式
"""
class Solution:
    # 定义：将以 root 为根的这棵二叉树翻转，返回翻转后的二叉树的根节点
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        leftTree = self.invertTree(root.left)
        rightTree = self.invertTree(root.right)

        root.left = rightTree
        root.right = leftTree

        return root
# leetcode submit region end(Prohibit modification and deletion)

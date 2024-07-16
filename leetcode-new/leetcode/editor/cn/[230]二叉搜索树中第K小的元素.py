"""
二叉搜索树中第K小的元素

# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数为 n 。 
#  1 <= k <= n <= 10⁴ 
#  0 <= Node.val <= 10⁴ 
#  
# 
#  
# 
#  进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？ 
# 
#  Related Topics树 | 深度优先搜索 | 二叉搜索树 | 二叉树 
# 
#  👍 872, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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
    def __init__(self):
        self.res = 0
        self.rank = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root, k)
        return self.res

    def traverse(self, root: Optional[TreeNode], k: int):
        if not root:
            return

        self.traverse(root.left, k)

        self.rank += 1
        if self.rank == k:
            self.res = root.val
            return

        self.traverse(root.right, k)
# leetcode submit region end(Prohibit modification and deletion)

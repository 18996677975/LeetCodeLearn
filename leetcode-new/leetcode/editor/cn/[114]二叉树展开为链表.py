"""
二叉树展开为链表

# 给你二叉树的根结点 root ，请你将它展开为一个单链表： 
# 
#  
#  展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。 
#  展开后的单链表应该与二叉树 先序遍历 顺序相同。 
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,5,3,4,null,6]
# 输出：[1,null,2,null,3,null,4,null,5,null,6]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中结点数在范围 [0, 2000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？ 
# 
#  Related Topics栈 | 树 | 深度优先搜索 | 链表 | 二叉树 
# 
#  👍 1686, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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

# 定义：输入节点 root，然后 root 为根的二叉树就会被拉平为一条链表
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.traverse(root)

    def traverse(self, root):
        if not root:
            return

        leftTree = self.traverse(root.left)
        rightTree = self.traverse(root.right)

        root.left = None
        root.right = leftTree

        p = root
        while p.right:
            p = p.right
        p.right = rightTree

        return root
# leetcode submit region end(Prohibit modification and deletion)

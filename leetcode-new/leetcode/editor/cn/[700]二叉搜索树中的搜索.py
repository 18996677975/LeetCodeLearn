"""
二叉搜索树中的搜索

# 给定二叉搜索树（BST）的根节点
#  root 和一个整数值
#  val。 
# 
#  你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回
#  null 。 
# 
#  
# 
#  示例 1: 
# 
#  
#  
# 
#  
# 输入：root = [4,2,7,1,3], val = 2
# 输出：[2,1,3]
#  
# 
#  示例 2: 
#  
#  
# 输入：root = [4,2,7,1,3], val = 5
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数在 [1, 5000] 范围内 
#  1 <= Node.val <= 10⁷ 
#  root 是二叉搜索树 
#  1 <= val <= 10⁷ 
#  
# 
#  Related Topics树 | 二叉搜索树 | 二叉树 
# 
#  👍 471, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 如果二叉树为空，直接返回
        if not root:
            return None
        # 去左子树搜索
        if root.val > val:
            return self.searchBST(root.left, val)
        # 去右子树搜索
        if root.val < val:
            return self.searchBST(root.right, val)
        # 找到目标节点，直接返回
        return root
# leetcode submit region end(Prohibit modification and deletion)

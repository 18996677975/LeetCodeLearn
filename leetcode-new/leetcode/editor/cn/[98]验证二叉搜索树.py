"""
验证二叉搜索树

# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。 
# 
#  有效 二叉搜索树定义如下： 
# 
#  
#  节点的左子树只包含 小于 当前节点的数。 
#  节点的右子树只包含 大于 当前节点的数。 
#  所有左子树和右子树自身必须也是二叉搜索树。 
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [2,1,3]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目范围在[1, 10⁴] 内 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  Related Topics树 | 深度优先搜索 | 二叉搜索树 | 二叉树 
# 
#  👍 2373, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, None, None)

    def isValidBSTHelper(self, root, min_node, max_node):
        # base case
        if not root:
            return True

        # 限定以 root 为根的子树节点必须满足 max.val > root.val > min.val
        if min_node and root.val <= min_node.val:
            return False

        if max_node and root.val >= max_node.val:
            return False

        # 限定左子树的最大值是 root.val，右子树的最小值是 root.val
        return (self.isValidBSTHelper(root.left, min_node, root)
                and self.isValidBSTHelper(root.right, root, max_node))
# leetcode submit region end(Prohibit modification and deletion)

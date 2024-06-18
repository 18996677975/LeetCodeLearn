"""
# 某公司架构以二叉树形式记录，请返回该公司的层级数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [1, 2, 2, 3, null, null, 5, 4, null, null, 4]
# 输出: 4
# 解释: 上面示例中的二叉树的最大深度是 4，沿着路径 1 -> 2 -> 3 -> 4 或 1 -> 2 -> 5 -> 4 到达叶节点的最长路径上有 4 
# 个节点。
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点总数 <= 10000 
#  
# 
#  注意：本题与主站 104 题相同：https://leetcode-cn.com/problems/maximum-depth-of-binary-
# tree/ 
# 
#  
# 
#  Related Topics树 | 深度优先搜索 | 广度优先搜索 | 二叉树 
# 
#  👍 269, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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
分解问题的方式
"""
class Solution:
    def calculateDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)

    def traverse(self, root):
        if not root:
            return 0

        leftDepth = self.traverse(root.left)
        rightDepth = self.traverse(root.right)

        return max(leftDepth, rightDepth) + 1

"""
遍历的方式
"""
class Solution:
    def __init__(self):
        self.depth = 0
        self.res = 0

    def calculateDepth(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return 0

        self.depth += 1

        if not root.left and not root.right:
            self.res = max(self.res, self.depth)

        self.traverse(root.left)
        self.traverse(root.right)

        self.depth -= 1
# leetcode submit region end(Prohibit modification and deletion)

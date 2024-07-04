"""
# 给你一棵二叉树的根节点 root ，返回所有 重复的子树 。 
# 
#  对于同一类的重复子树，你只需要返回其中任意 一棵 的根结点即可。 
# 
#  如果两棵树具有 相同的结构 和 相同的结点值 ，则认为二者是 重复 的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [1,2,3,4,null,2,4,null,null,4]
# 输出：[[2,4],[4]] 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root = [2,1,1]
# 输出：[[1]] 
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：root = [2,2,2,3,null,3,null]
# 输出：[[2,3],[3]] 
# 
#  
# 
#  提示： 
# 
#  
#  树中的结点数在 [1, 5000] 范围内。 
#  -200 <= Node.val <= 200 
#  
# 
#  Related Topics树 | 深度优先搜索 | 哈希表 | 二叉树 
# 
#  👍 749, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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
class Solution:
    def __init__(self):
        # 记录重复的子树根节点
        self.res = []
        # 记录所有子树以及出现的次数
        self.subTree = {}

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.traverse(root)
        return self.res

    def traverse(self, root: Optional[TreeNode]):
        if not root:
            return "#"

        # 先算左右子树的序列化结果
        left = self.traverse(root.left)
        right = self.traverse(root.right)

        tree = left + "," + right + "," + str(root.val)

        times = self.subTree.get(tree, 0)
        # 多次重复也只会被加入结果集一次
        if times == 1:
            self.res.append(root)
        # 给子树对应的出现次数加一
        self.subTree[tree] = times + 1

        return tree

# leetcode submit region end(Prohibit modification and deletion)

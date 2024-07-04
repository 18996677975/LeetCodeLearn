"""
# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并
# 返回这颗 二叉树 。 
# 
#  
# 
#  示例 1: 
#  
#  
# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# 输入：inorder = [-1], postorder = [-1]
# 输出：[-1]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= inorder.length <= 3000 
#  postorder.length == inorder.length 
#  -3000 <= inorder[i], postorder[i] <= 3000 
#  inorder 和 postorder 都由 不同 的值组成 
#  postorder 中每一个值都在 inorder 中 
#  inorder 保证是树的中序遍历 
#  postorder 保证是树的后序遍历 
#  
# 
#  Related Topics树 | 数组 | 哈希表 | 分治 | 二叉树 
# 
#  👍 1236, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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
        self.valToIndex = {}

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.valToIndex[inorder[i]] = i
        return self.build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def build(self, inorder: List[int], inoStart: int, inoEnd: int, postorder: List[int], postStart: int, postEnd: int):
        if postStart > postEnd:
            return None

        rootVal = postorder[postEnd]

        index = self.valToIndex.get(rootVal)

        leftSize = index - inoStart

        root = TreeNode(rootVal)

        root.left = self.build(inorder, inoStart, index - 1, postorder, postStart, postStart + leftSize - 1)
        root.right = self.build(inorder, index + 1, inoEnd, postorder, postStart + leftSize, postEnd - 1)

        return root
# leetcode submit region end(Prohibit modification and deletion)

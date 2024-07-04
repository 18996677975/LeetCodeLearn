"""
# 给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder 是同一棵
# 树的后序遍历，重构并返回二叉树。 
# 
#  如果存在多个答案，您可以返回其中 任何 一个。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# 输出：[1,2,3,4,5,6,7]
#  
# 
#  示例 2: 
# 
#  
# 输入: preorder = [1], postorder = [1]
# 输出: [1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= preorder.length <= 30 
#  1 <= preorder[i] <= preorder.length 
#  preorder 中所有值都 不同 
#  postorder.length == preorder.length 
#  1 <= postorder[i] <= postorder.length 
#  postorder 中所有值都 不同 
#  保证 preorder 和 postorder 是同一棵二叉树的前序遍历和后序遍历 
#  
# 
#  Related Topics树 | 数组 | 哈希表 | 分治 | 二叉树 
# 
#  👍 387, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(postorder)):
            self.valToIndex[postorder[i]] = i
        return self.build(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1)

    def build(self, preorder: List[int], preStart: int, preEnd: int, postorder: List[int], postStart: int, postEnd: int):
        if preStart > preEnd:
            return None
        if preStart == preEnd:
            return TreeNode(preorder[preStart])

        # root 节点对应的值就是前序遍历数组的第一个元素
        rootVal = preorder[preStart]
        # root.left 的值是前序遍历第二个元素
        # 通过前序和后序遍历构造二叉树的关键在于通过左子树的根节点
        # 确定 preorder 和 postorder 中左右子树的元素区间
        nextRootVal = preorder[preStart + 1]

        index = self.valToIndex.get(nextRootVal)

        leftSize = index - postStart + 1

        root = TreeNode(rootVal)
        root.left = self.build(preorder, preStart + 1, preStart + leftSize, postorder, postStart, index)
        root.right = self.build(preorder, preStart + leftSize + 1, preEnd, postorder, index + 1, postEnd - 1)

        return root
# leetcode submit region end(Prohibit modification and deletion)

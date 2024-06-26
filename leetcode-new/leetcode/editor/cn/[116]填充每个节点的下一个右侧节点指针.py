"""
填充每个节点的下一个右侧节点指针

# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下： 
# 
#  
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# } 
# 
#  填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。 
# 
#  初始状态下，所有 next 指针都被设置为 NULL。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [1,2,3,4,5,6,7]
# 输出：[1,#,2,3,#,4,5,6,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 
# next 指针连接，'#' 标志着每一层的结束。
#  
# 
#  
#  
# 
#  示例 2: 
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
#  树中节点的数量在
#  [0, 2¹² - 1] 范围内 
#  -1000 <= node.val <= 1000 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你只能使用常量级额外空间。 
#  使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。 
#  
# 
#  Related Topics树 | 深度优先搜索 | 广度优先搜索 | 链表 | 二叉树 
# 
#  👍 1121, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""
from collections import deque
from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""
1、层序遍历 方式
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return

        dq = deque()
        dq.append(root)

        while dq:
            sz = len(dq)
            tmp = []
            for i in range(sz):
                cur = dq.popleft()
                tmp.append(cur)
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            for i in range(sz):
                if i == sz - 1:
                    tmp[i].next = None
                else:
                    tmp[i].next = tmp[i + 1]

        return root

"""
2、深度优先 方式
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        self.traverse(root.left, root.right)

        return root

    def traverse(self, leftNode, rightNode):
        if not leftNode or not rightNode:
            return

        leftNode.next = rightNode

        self.traverse(leftNode.left, leftNode.right)
        self.traverse(rightNode.left, rightNode.right)
        self.traverse(leftNode.right, rightNode.left)

# leetcode submit region end(Prohibit modification and deletion)

"""
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方
# 式重构得到原数据。 
# 
#  请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串
# 反序列化为原始的树结构。 
# 
#  提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的
# 方法解决这个问题。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
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
# 输入：root = [1]
# 输出：[1]
#  
# 
#  示例 4： 
# 
#  
# 输入：root = [1,2]
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中结点数在范围 [0, 10⁴] 内 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics树 | 深度优先搜索 | 广度优先搜索 | 设计 | 字符串 | 二叉树 
# 
#  👍 1226, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""
from collections import deque
from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

NULL = "#"
SEP = ","

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        sb = []
        self.serialize_helper(root, sb)
        return "".join(sb)

    def serialize_helper(self, root, sb):
        if not root:
            sb.append(NULL)
            sb.append(SEP)
            return

        sb.append(str(root.val))
        sb.append(SEP)

        self.serialize_helper(root.left, sb)
        self.serialize_helper(root.right, sb)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = deque(data.split(SEP))
        return self.deserialize_helper(nodes)

    def deserialize_helper(self, nodes):
        if not nodes:
            return None

        first = nodes.popleft()
        if first == NULL:
            return None

        root = TreeNode(int(first))
        root.left = self.deserialize_helper(nodes)
        root.right = self.deserialize_helper(nodes)

        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)

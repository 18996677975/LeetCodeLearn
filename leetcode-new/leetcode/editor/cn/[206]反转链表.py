"""
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# 
#  
#  
#  
#  
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
#  
# 
#  示例 2： 
#  
#  
# 输入：head = [1,2]
# 输出：[2,1]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目范围是 [0, 5000] 
#  -5000 <= Node.val <= 5000 
#  
# 
#  
# 
#  进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？ 
# 
#  Related Topics递归 | 链表 
# 
#  👍 3601, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
1、迭代的方式
"""
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#
#         fast, slow = head.next, head
#
#         while fast:
#             next_fast = fast.next
#             fast.next = slow
#             slow = fast
#             fast = next_fast
#
#         head.next = None
#
#         return slow

"""
2、递归的方式
"""
class Solution:
    # 定义：输入一个单链表头节点，将该链表反转，返回新的头结点
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return last
# leetcode submit region end(Prohibit modification and deletion)

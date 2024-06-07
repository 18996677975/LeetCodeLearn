"""
移除链表元素

# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [], val = 1
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [7,7,7,7], val = 7
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  列表中的节点数目在范围 [0, 10⁴] 内 
#  1 <= Node.val <= 50 
#  0 <= val <= 50 
#  
# 
#  Related Topics递归 | 链表 
# 
#  👍 1426, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 空链表直接返回
        if not head:
            return head

        # 删除开始就等于 val 的节点
        while head and head.val == val:
            head = head.next

        # 如果所有数值都是 val，全部删除后 链表为空，直接返回
        if not head:
            return head

        # 正常进行 val 值节点删除
        p1, p2 = head, head.next
        while p2:
            if p2.val == val:
                p1.next = p2.next
            else:
                p1 = p1.next
            p2 = p2.next

        return head
# leetcode submit region end(Prohibit modification and deletion)

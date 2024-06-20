"""
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,2,1]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：head = [1,2]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目在范围[1, 10⁵] 内 
#  0 <= Node.val <= 9 
#  
# 
#  
# 
#  进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
# 
#  Related Topics栈 | 递归 | 链表 | 双指针 
# 
#  👍 1916, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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
1、全量对比的方式
"""
# class Solution:
#     left = None   # 从左往右移动的指针
#     right = None  # 从右往左移动的指针
#     res = True
#
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         self.left = head
#         self.traverse(head)
#         return self.res
#
#     def traverse(self, right):
#         if not right:
#             return
#
#         self.traverse(right.next)
#
#         if self.left.val != right.val:
#             self.res = False
#
#         self.left = self.left.next

"""
2、反转链表，部分对比的方式
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if fast:
            slow = slow.next

        left, right = head, self.reverse(slow)

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

    def reverse(self, head):
        pre, cur = None, head

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre
# leetcode submit region end(Prohibit modification and deletion)

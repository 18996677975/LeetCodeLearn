"""
# 给定两个以 有序链表 形式记录的训练计划 l1、l2，分别记录了两套核心肌群训练项目编号，请合并这两个训练计划，按训练项目编号 升序 记录于链表并返回。 
# 
#  注意：新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4] 
# 
#  示例 2： 
# 
#  
# 输入：l1 = [], l2 = []
# 输出：[] 
# 
#  示例 3： 
# 
#  
# 输入：l1 = [], l2 = [0]
# 输出：[0] 
# 
#  
# 
#  提示： 
# 
#  0 <= 链表长度 <= 1000 
# 
#  
# 
#  注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/ 
# 
#  
# 
#  Related Topics递归 | 链表 
# 
#  👍 389, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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
    def trainningPlan(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        p1, p2 = l1, l2
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
                p = p.next
            else:
                p.next = p2
                p2 = p2.next
                p = p.next

        if p1:
            p.next = p1
        if p2:
            p.next = p2

        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)

"""
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。 
# 
#  k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
#  
# 
#  
# 提示：
# 
#  
#  链表中的节点数目为 n 
#  1 <= k <= n <= 5000 
#  0 <= Node.val <= 1000 
#  
# 
#  
# 
#  进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？ 
# 
#  
#  
# 
#  Related Topics递归 | 链表 
# 
#  👍 2343, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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


def reverseLR(left, right):
    pre, cur, nxt = None, left, left
    while cur != right:
        nxt = cur.next
        # 逐个结点反转
        cur.next = pre
        # 更新指针位置
        pre = cur
        cur = nxt
    # 返回反转后的头结点
    return pre


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        # 区间 [left, right) 包含 k 个待反转元素
        left, right = head, head

        for i in range(k):
            # 不足 k 个，不需要反转，base case
            if not right:
                return head
            right = right.next

        new_head = reverseLR(left, right)
        left.next = self.reverseKGroup(right, k)

        return new_head
# leetcode submit region end(Prohibit modification and deletion)

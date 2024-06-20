"""
# 给定一个链表的第一个节点 head ，找到链表中所有出现多于一次的元素，并删除这些元素所在的节点。 
# 
#  返回删除后的链表。 
# 
#  
# 
#  示例 1: 
#  输入: head = [1,2,3,2]
# 输出: [1,3]
# 解释: 2 在链表中出现了两次，所以所有的 2 都需要被删除。删除了所有的 2 之后，我们还剩下 [1,3] 。
#  
# 
#  示例 2: 
#  输入: head = [2,1,1,2]
# 输出: []
# 解释: 2 和 1 都出现了两次。所有元素都需要被删除。
#  
# 
#  示例 3: 
#  输入: head = [3,2,2,1,3,2,4]
# 输出: [1,4]
# 解释: 3 出现了两次，且 2 出现了三次。移除了所有的 3 和 2 后，我们还剩下 [1,4] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点个数的范围是 [1, 10⁵] 
#  1 <= Node.val <= 10⁵ 
#  
# 
#  Related Topics哈希表 | 链表 
# 
#  👍 21, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        p = head
        nodes = dict()

        while p:
            nodes[p.val] = nodes.get(p.val, 0) + 1
            p = p.next

        p = head
        dummy = ListNode(-1)
        q = dummy

        while p:
            if nodes.get(p.val) == 1:
                q.next = p
                q = q.next
            p = p.next
        q.next = None

        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)

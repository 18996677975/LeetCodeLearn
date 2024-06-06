"""
# 给定一个头节点为 head 的链表用于记录一系列核心肌群训练项目编号，请查找并返回倒数第 cnt 个训练项目编号。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [2,4,7,8], cnt = 1
# 输出：8 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= head.length <= 100 
#  0 <= head[i] <= 100 
#  1 <= cnt <= head.length 
#  
# 
#  
# 
#  Related Topics链表 | 双指针 
# 
#  👍 514, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
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
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        fast, slow = head, head

        for i in range(cnt):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        return slow
# leetcode submit region end(Prohibit modification and deletion)

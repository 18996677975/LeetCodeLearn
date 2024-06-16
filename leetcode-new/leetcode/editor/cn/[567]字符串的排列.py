"""
字符串的排列

# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。 
# 
#  换句话说，s1 的排列之一是 s2 的 子串 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#  
# 
#  示例 2： 
# 
#  
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s1.length, s2.length <= 10⁴ 
#  s1 和 s2 仅包含小写字母 
#  
# 
#  Related Topics哈希表 | 双指针 | 字符串 | 滑动窗口 
# 
#  👍 1007, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need, window = dict(), dict()
        for c in s1:
            need[c] = need.get(c, 0) + 1

        l, r = 0, 0
        v = 0

        while r < len(s2):
            c = s2[r]
            r += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    v += 1

            while r - l == len(s1):
                if v == len(need):
                    return True

                d = s2[l]
                l += 1
                if d in need:
                    if window[d] == need[d]:
                        v -= 1
                    window[d] -= 1

        return False
# leetcode submit region end(Prohibit modification and deletion)

"""
最长回文子串

# 给你一个字符串 s，找到 s 中最长的 回文 子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母组成 
#  
# 
#  Related Topics双指针 | 字符串 | 动态规划 
# 
#  👍 7246, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            s1 = self.isPalindrome(s, i, i)
            s2 = self.isPalindrome(s, i, i + 1)
            res = s1 if len(s1) > len(res) else res
            res = s2 if len(s2) > len(res) else res

        return res

    def isPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

# leetcode submit region end(Prohibit modification and deletion)

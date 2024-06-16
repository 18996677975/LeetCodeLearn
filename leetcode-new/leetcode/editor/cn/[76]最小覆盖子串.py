"""
最小覆盖子串

# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。 
# 
#  
# 
#  注意： 
# 
#  
#  对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。 
#  如果 s 中存在这样的子串，我们保证它是唯一的答案。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。 
# 
#  
# 
#  提示： 
# 
#  
#  m == s.length 
#  n == t.length 
#  1 <= m, n <= 10⁵ 
#  s 和 t 由英文字母组成 
#  
# 
#  
# 进阶：你能设计一个在 
# o(m+n) 时间内解决此问题的算法吗？
# 
#  Related Topics哈希表 | 字符串 | 滑动窗口 
# 
#  👍 2918, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = dict(), dict()
        for c in t:
            need[c] = need.get(c, 0) + 1

        l, r = 0, 0
        v = 0
        start, length = 0, 10 ** 5 + 1

        while r < len(s):
            c = s[r]
            r += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if need[c] == window[c]:
                    v += 1

            while v == len(need):
                if r - l < length:
                    start = l
                    length = r - l

                d = s[l]
                l += 1

                if d in need:
                    if need[d] == window[d]:
                        v -= 1
                    window[d] -= 1

        return "" if length == (10 ** 5 + 1) else s[start:start + length]

# leetcode submit region end(Prohibit modification and deletion)

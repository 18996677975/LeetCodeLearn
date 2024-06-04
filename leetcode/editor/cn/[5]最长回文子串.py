"""
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
#  👍 7233, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            s1 = self.isPalindrome(s, i, i)
            s2 = self.isPalindrome(s, i, i+1)

            # print("s1: " + s1)
            # print("s2: " + s2)

            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2

        return res

    def isPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 跳出循环时就不满足 回文 条件了，因此要获取 left+1~right-1 区间的数据，切片是左闭右开的区间，因此写为 s[left + 1 : right]
        return s[left + 1 : right]
# leetcode submit region end(Prohibit modification and deletion)

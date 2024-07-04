"""
重复的DNA序列

# DNA序列 由一系列核苷酸组成，缩写为
#  'A', 'C', 'G' 和
#  'T'.。 
# 
#  
#  例如，
#  "ACGAATTCCG" 是一个 DNA序列 。 
#  
# 
#  在研究 DNA 时，识别 DNA 中的重复序列非常有用。 
# 
#  给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 10⁵ 
#  s[i]=='A'、'C'、'G' or 'T' 
#  
# 
#  Related Topics位运算 | 哈希表 | 字符串 | 滑动窗口 | 哈希函数 | 滚动哈希 
# 
#  👍 589, 👎 0bug 反馈 | 使用指南 | 更多配套插件 
# 
# 
# 
# 

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # 先把字符串转化成四进制的数字数组
        nums = [0] * len(s)
        for i in range(len(nums)):
            if s[i] == 'A':
                nums[i] = 0
            elif s[i] == 'G':
                nums[i] = 1
            elif s[i] == 'C':
                nums[i] = 2
            elif s[i] == 'T':
                nums[i] = 3

        # 记录重复出现的哈希值
        seen = set()
        # 记录重复出现的字符串结果
        res = set()

        # 数字位数
        L = 10
        # 进制
        R = 4
        # 存储 R^(L - 1) 的结果
        RL = R ** (L - 1)
        # 维护滑动窗口中字符串的哈希值
        windowHash = 0

        # 滑动窗口代码框架，时间 O(N)
        left, right = 0, 0
        while right < len(nums):
            # 扩大窗口，移入字符，并维护窗口哈希值（在最低位添加数字）
            windowHash = R * windowHash + nums[right]
            right += 1

            # 当子串的长度达到要求
            if right - left == L:
                # 根据哈希值判断是否曾经出现过相同的子串
                if windowHash in seen:
                    # 当前窗口中的子串是重复出现的
                    res.add(s[left:right])
                else:
                    # 当前窗口中的子串之前没有出现过，记下来
                    seen.add(windowHash)
                # 缩小窗口，移出字符，并维护窗口哈希值（删除最高位数字）
                windowHash -= nums[left] * RL
                left += 1

        return list(res)
# leetcode submit region end(Prohibit modification and deletion)

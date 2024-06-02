# 给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（ 包括重复字符），并以数组形式返回。你可以按 任意顺序 返回答
# 案。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：words = ["bella","label","roller"]
# 输出：["e","l","l"]
#  
# 
#  示例 2： 
# 
#  
# 输入：words = ["cool","lock","cook"]
# 输出：["c","o"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 100 
#  1 <= words[i].length <= 100 
#  words[i] 由小写英文字母组成 
#  
# 
#  Related Topics 数组 哈希表 字符串 👍 368 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        keys = [chr(i) for i in range(97, 123)]
        dicts = []
        for word in words:
            tmp = {}
            for i in range(len(word)):
                tmp[word[i]] = tmp.get(word[i], 0) + 1
            dicts.append(tmp)

        for key in keys:
            tmp = []
            for d in dicts:
                tmp.append(d.get(key, 0))
            for i in range(min(tmp)):
                res.append(key)
        return res
# leetcode submit region end(Prohibit modification and deletion)

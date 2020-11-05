# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。 
# 
#  说明： 
# 
#  
#  拆分时可以重复使用字典中的单词。 
#  你可以假设字典中没有重复的单词。 
#  
# 
#  示例 1： 
# 
#  输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
#  
# 
#  示例 2： 
# 
#  输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
#  
# 
#  示例 3： 
# 
#  输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#  
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic, max_len = {}, 0
        # 将单词放入字典，同时得到最长单词长度
        for word in wordDict:
            max_len = max(max_len, len(word))
            dic[word] = len(word)
        length = len(s)
        # 多出一个dp[0]为basecase，不对应s中任何字符，因此dp长度为length+1
        # dp[i]是到s[i-1]为止，是否正好切分成wordDict中单词
        dp = [False] * (length + 1)
        dp[0] = True
        # 注意好各个边界值！
        for i in range(length):
            # 剪枝，每次从i+1遍历到最大单词长度处，不用每次都遍历到s结尾
            for j in range(i + 1, min(i + max_len + 1, length + 1)):
                if dp[i] and (s[i:j] in dic):
                    dp[j] = True
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)

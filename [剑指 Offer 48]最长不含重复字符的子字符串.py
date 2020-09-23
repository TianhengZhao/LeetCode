# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。 
# 
#  
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  s.length <= 40000 
#  
# 
#  注意：本题与主站 3 题相同：https://leetcode-cn.com/problems/longest-substring-without-rep
# eating-characters/ 
#  Related Topics 哈希表 双指针 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring_1(self, s: str) -> int:
        hashmap = {}
        res, left = 0, -1
        for right in range(len(s)):
            if s[right] in hashmap:
                left = max(hashmap[s[right]], left)
            res = max(res, right - left)
            hashmap[s[right]] = right
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        i从头遍历字符串
        tmp存储不含重复字符的子串
        如果s[i]出现过，删除tmp中从头到s[i]的子串
        cal为每个子串长度
        """
        if len(s) <= 1:
            return len(s)
        tmp = [s[0]]
        res = cal = 1
        for i in range(1, len(s)):
            if s[i] in tmp:
                res = max(cal, res)
                for j in range(len(tmp)):
                    if tmp[j] == s[i]:
                        break
                del tmp[:j + 1]
                cal = len(tmp) + 1
            else:
                cal += 1
            tmp.append(s[i])
        return max(res, cal)
# leetcode submit region end(Prohibit modification and deletion)

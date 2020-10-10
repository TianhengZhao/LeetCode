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
        """双指针，right每次向右移动一个值，left固定在最新的重复值处"""
        hashmap = {}
        res, left = 0, -1
        for right in range(len(s)):
            if s[right] in hashmap:
                # s[right]可能存在于head左侧，所以取max
                left = max(hashmap[s[right]], left)
            # 对于每个right更新一次res
            res = max(res, right - left)
            hashmap[s[right]] = right
        return res
# leetcode submit region end(Prohibit modification and deletion)

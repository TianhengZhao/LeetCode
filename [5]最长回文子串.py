# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome_1(self, s: str) -> str:
        """动态规划"""
        length = len(s)
        # dp[i][j]为子串s[i:j+1]是否为回文串
        dp = [[False] * length for _ in range(length)]
        left, right = 0, 0
        # 矩阵上三角去掉对角线部分
        # 从左往右一列一列地看；若是按行看，需要从下往上，否则dp[i + 1][j - 1]会取得错误值
        for j in range(1, length):
            for i in range(j):
                # 边界，子串长度为2或3，只需比较首末两字符
                if j - i < 3:
                    dp[i][j] = s[i] == s[j]
                # 先判断首末两字符，若相等，看其去掉首末两字符的子串是否相等
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
                # 若该子串为回文串，判断其长度
                if dp[i][j]:
                    if j - i >= right - left:
                        left, right = i, j
        # 如果没有回文串，返回s第一个字符，left, right = 0, 0
        return s[left: right + 1]

# leetcode submit region end(Prohibit modification and deletion)

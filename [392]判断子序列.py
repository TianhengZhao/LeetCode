# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。 
# 
#  你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。 
# 
#  字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"ae
# c"不是）。 
# 
#  示例 1: 
# s = "abc", t = "ahbgdc" 
# 
#  返回 true. 
# 
#  示例 2: 
# s = "axc", t = "ahbgdc" 
# 
#  返回 false. 
# 
#  后续挑战 : 
# 
#  如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码
# ？
#  Related Topics 贪心算法 二分查找 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """双指针"""
        p1 = p2 = 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        return p1 == len(s)

    def isSubsequence_ans(self, s: str, t: str) -> bool:
        """
        建立(len(t)+ 1)×26的二维数组，存放某一状态下各个字母在t中的位置
        pos[i][j]表示t中，在位置i及i以后，字母j第一次出现的位置
        最后一行为无穷大，即该行t已结束，无匹配值
        """
        m = len(t)
        pos = [[0] * 26 for _ in range(m)]
        # 用m表示无穷大，即不会到达的位置值
        pos.append([m] * 26)
        # 从后向前对每个字母位置进行更新
        for i in range(m - 1, -1, -1):
            for j in range(0, 26):
                # 每行更新一个值
                if j == ord(t[i]) - 97:
                    pos[i][j] = i
                # 其余值和i+1行相等
                else:
                    pos[i][j] = pos[i + 1][j]
        i = 0
        for char in s:
            # 无匹配
            if pos[i][ord(char) - 97] == m:
                return False
            else:
                # 匹配，查找s下一字母是否匹配
                i = pos[i][ord(char) - 97] + 1
        return True
# leetcode submit region end(Prohibit modification and deletion)

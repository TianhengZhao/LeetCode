# 给定两个字符串 s 和 t，它们只包含小写字母。 
# 
#  字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。 
# 
#  请找出在 t 中被添加的字母。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "abcd", t = "abcde"
# 输出："e"
# 解释：'e' 是那个被添加的字母。
#
#  提示： 
# 
#  
#  0 <= s.length <= 1000 
#  t.length == s.length + 1 
#  s 和 t 只包含小写字母 
#  
#  Related Topics 位运算 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = collections.defaultdict(int)
        for c in s:
            dic[c] += 1
        for c in t:
            if dic[c] == 0:
                return c
            else:
                dic[c] -= 1

    def findTheDifference1(self, s: str, t: str) -> str:
        sum1, sum2 = 0, 0
        for c in s:
            sum1 += ord(c)
        for c in t:
            sum2 += ord(c)
        return chr(sum2 - sum1)
# leetcode submit region end(Prohibit modification and deletion)

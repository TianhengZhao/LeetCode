# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。 
# 
#  注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct
# -characters 相同 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "bcabc"
# 输出："abc"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbacdcbc"
# 输出："acdb" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 104 
#  s 由小写英文字母组成 
#  
#  Related Topics 栈 贪心算法 字符串


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def removeDuplicateLettersAns(self, s: str) -> str:
        """贪心+栈"""
        counts = Counter(s)
        stack = []
        for char in s:
            # char已经排在了其合适的位置
            if char in stack:
                counts[char] -= 1
            else:
                # 字符逆序
                while stack and stack[-1] > char:
                    # 如果栈顶字符不重复
                    if counts[stack[-1]] == 1:
                        break
                    # 后面还有该栈顶字符出现，删除此栈顶字符，消除此处逆序
                    else:
                        counts[stack[-1]] -= 1
                        stack.pop()
                stack.append(char)
        return ''.join(stack)
# leetcode submit region end(Prohibit modification and deletion)

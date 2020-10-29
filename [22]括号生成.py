# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.backtrack('', n, n)
        return self.res

    def backtrack(self, cur, left, right):
        """
        :param cur: 当前的括号字符串
        :param left:剩余的左括号数
        :param right:剩余的右括号数
        :return:
        """
        if left == 0 and right == 0:
            self.res.append(cur)
            return
        if left > 0:
            self.backtrack(cur + '(', left - 1, right)
        if right > left:
            self.backtrack(cur + ')', left, right - 1)
# leetcode submit region end(Prohibit modification and deletion)

# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。 
# 
#  首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下： 
# 
#  
#  如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。 
#  假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。 
#  该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。 
#  
# 
#  注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。 
# 
#  在任何情况下，若函数不能进行有效的转换时，请返回 0 。 
# 
#  提示： 
# 
#  
#  本题中的空白字符只包括空格字符 ' ' 。 
#  假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231, 231 − 1]。如果数值超过这个范围，请返回 INT_MAX (231
#  − 1) 或 INT_MIN (−231) 。 
#  

#  输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
#
# 
#  输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
#      因此返回 INT_MIN (−231) 。
#  
#  Related Topics 数学 字符串


# leetcode submit region begin(Prohibit modification and deletion)
INT_MAX, INT_MIN = 2 ** 31 - 1, -2 ** 31


class Atomation:
    def __init__(self):
        self.state = 'start'
        self.sig = 1
        self.res = 0
        # 四种情况分别是遇到 空格、+/-、数字、其他
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }

    def change_state(self, char):
        # 更新状态
        self.state = self.table[self.state][self.cal_col(char)]
        if self.state == 'in_number':
            self.res = self.res * 10 + int(char)
            if self.sig * self.res < INT_MIN:
                self.res = -INT_MIN
            elif self.sig * self.res > INT_MAX:
                self.res = INT_MAX
        elif self.state == 'signed':
            self.sig = -1 if char == '-' else 1

    def cal_col(self, char):
        """根据本轮的char得到table中状态索引"""
        if char == ' ':
            return 0
        if char == '+' or char == '-':
            return 1
        if ord('0') <= ord(char) <= ord('9'):
            return 2
        return 3


class Solution:
    def myAtoiAns(self, s: str) -> int:
        """有限状态自动机"""
        auto = Atomation()
        for c in s:
            auto.change_state(c)
        return auto.res * auto.sig

    def myAtoi1(self, s: str) -> int:
        """
        普通判断
        """
        # 去空格
        s = s.strip()
        if not len(s):
            return 0
        res, cnt, sig = 0, 0, 1
        # 判断符号，用sig记录
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sig = -1
            cnt += 1
        while cnt < len(s) and 48 <= ord(s[cnt]) <= 57:
            # 计算数字
            res = res * 10 + int(s[cnt])
            if sig * res < INT_MIN:
                return INT_MIN
            elif sig * res > INT_MAX:
                return INT_MAX
            cnt += 1
        return res * sig

# leetcode submit region end(Prohibit modification and deletion)

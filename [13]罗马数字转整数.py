# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。 
# 
#  字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000 
# 
#  例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做 XXVII, 即为 XX + V + I
# I 。 
# 
#  通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5
#  减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况： 
# 
#  
#  I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。 
#  X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
#  C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。 
#  
# 
#  给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。 
# 
#  Related Topics 数学 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def romanToInt_mine(self, s: str) -> int:
        """
        先判断是否有特殊字符
        删除特殊字符，对剩余进行加和
        93.81% ； 6.45%
        """
        spe = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        rule = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for (r, score) in spe.items():
            pos = s.find(r)
            if pos != -1:
                res += score
                s = s[:pos] + s[pos+2:]
                pos = -1
        for i in s:
            if i in rule:
                res += rule[i]
        return res

    def romanToInt_other(self, s: str) -> int:
        """
        左边字符比右边的小，减掉；否则相加
        """
        roman2int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0

        for index in range(len(s)-1):
            if roman2int[s[index]] < roman2int[s[index + 1]]:
                res -= roman2int[s[index]]
            else:
                res += roman2int[s[index]]

        return res + roman2int[s[-1]]



# leetcode submit region end(Prohibit modification and deletion)

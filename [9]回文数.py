# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。 
#
#  进阶: 
# 
#  你能不将整数转为字符串来解决这个问题吗？ 
#  Related Topics 数学 



# leetcode submit region begin(Prohibit modification and deletion)
from math import ceil


class Solution:
    def isPalindrome_mine1(self, x: int) -> bool:
        """
        转换成字符串
        用一个列表前一半和后一半对比
        """
        if x < 0:
            return False
        ls = list(str(x))
        for i in range(ceil(len(ls)/2)):
            if ls[i] != ls[len(ls)-i-1]:
                return False
        return True

    def isPalindrome_mine2(self, x: int) -> bool:
        """
        整数反转，数学方法
        不用转换成字符串的方法
        """
        if x < 0:
            return False
        res = 0
        y = x
        while y != 0:
            res = 10 * res + y % 10
            y //= 10
        if res == x:
            return True
        else:
            return False

    def isPalindrome_mine3(self, x: int) -> bool:
        """
        转换成字符串
        列表逆序后与原列表对比
        效率最高
        """
        if x < 0:
            return False
        ls = list(str(x))
        if ls == ls[::-1]:
            return True
        else:
            return False

    def isPalindrome_others(self, x: int) -> bool:
        """
        转化成字符串，翻转后比较
        """
        if x < 0:
            return False
        else:
            y = str(x)[::-1]
            if y == str(x):
                return True
            else:
                return False

# leetcode submit region end(Prohibit modification and deletion)

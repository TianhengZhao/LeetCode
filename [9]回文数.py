# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。 
#
#  进阶: 
# 
#  你能不将整数转为字符串来解决这个问题吗？ 
#  Related Topics 数学 



# leetcode submit region begin(Prohibit modification and deletion)
from math import ceil


class Solution:
    def isPalindrome1(self, x: int) -> bool:
        """
        转换成字符串
        头尾两个指针作比较
        """
        if x < 0:
            return False
        ls = str(x)
        for i in range(len(ls) // 2):
            if ls[i] != ls[len(ls)-i-1]:
                return False
        return True

    def isPalindrome2(self, x: int) -> bool:
        """
        整数反转，数学方法
        不用转换成字符串的方法
        """
        if x < 0:
            return False
        res, y = 0, x
        while y != 0:
            res = 10 * res + y % 10
            y //= 10
        return True if res == x else False

    def isPalindrome3(self, x: int) -> bool:
        """
        转换成字符串
        列表逆序后与原列表对比
        """
        if x < 0:
            return False
        ls = str(x)
        return True if ls == ls[::-1] else False



# leetcode submit region end(Prohibit modification and deletion)

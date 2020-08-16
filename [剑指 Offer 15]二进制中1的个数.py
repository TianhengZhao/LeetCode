# 请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 
# 2。 
# 
#  示例 1： 
# 
#  输入：00000000000000000000000000001011
# 输出：3
# 解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
#
#  
# 
#  注意：本题与主站 191 题相同：https://leetcode-cn.com/problems/number-of-1-bits/ 
#  Related Topics 位运算


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hammingWeight_1(self, n: int) -> int:
        """转换成二进制"""
        res = 0
        while n != 0:
            if n % 2:
                res += 1
            n = n // 2
        return res

    def hammingWeight_2(self, n: int) -> int:
        """
        & 按位与
        """
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

    def hammingWeight_3(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            # 消去n的最后一位1
            # 初始n有几个1，消几次，最后n为0
            n &= n - 1
        return res
        
# leetcode submit region end(Prohibit modification and deletion)

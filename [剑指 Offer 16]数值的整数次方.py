# 实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数
# 问题。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 2.00000, 10
# 输出: 1024.00000
#  
# 
#  示例 2: 
# 
#  输入: 2.10000, 3
# 输出: 9.26100
#  
# 
#  示例 3: 
# 
#  输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25 
# 
#  
# 
#  说明: 
# 
#  
#  -100.0 < x < 100.0 
#  n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。 
#  
# 
#  注意：本题与主站 50 题相同：https://leetcode-cn.com/problems/powx-n/ 
#  Related Topics 递归


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def myPow_1(self, x: float, n: int) -> float:
        """递归 O（log n）"""
        if x == 0:
            return 0
        if n < 0:
            x, n = 1 / x, -n
        return self.pow(x, n)

    def pow(self, x, n):
        if n == 0:
            return 1
        num = self.pow(x, n // 2)
        if n % 2:
            return x * num * num
        return num * num


    def myPow_2(self, x: float, n: int) -> float:
        """
        迭代
        x -> x^2 -> x^4 --(x)-> x^9 --(x)-> x^19 -> x^38 --(x)-> x^77
        1001101
        对应x^64 * x^8 * x^4 * x
        https://leetcode-cn.com/problems/powx-n/solution/powx-n-by-leetcode-solution/
        """
        if x == 0:
            return 0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            # 如果二进制中该位为1
            if n & 1:
                res *= x
            x *= x
            n >>= 2
        return res
# leetcode submit region end(Prohibit modification and deletion)

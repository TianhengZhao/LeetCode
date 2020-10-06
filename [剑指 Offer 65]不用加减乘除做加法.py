# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。 
# 
#  
# 
#  示例: 
# 
#  输入: a = 1, b = 1
# 输出: 2 
#
#  a, b 均可能是负数或 0 
#  结果不会溢出 32 位整数


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def add(self, a: int, b: int) -> int:
        """位运算求两数之和"""
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)
# leetcode submit region end(Prohibit modification and deletion)

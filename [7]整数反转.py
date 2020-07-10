# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。 
#
#  注意: 
# 
#  假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231, 231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。 
#


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        """
        通过逻辑左移判断边界，由于将数值取绝对值，边界也是绝对值
        通过数学计算得到结果值
        """
        temp, b = abs(x), 0
        boundry = (1 << 31) - 1 if x > 0 else (1 << 31)
        while temp != 0:
            b = 10 * b + temp % 10
            temp //= 10
            if b > boundry:
                return 0
        return b if x > 0 else -b
# leetcode submit region end(Prohibit modification and deletion)

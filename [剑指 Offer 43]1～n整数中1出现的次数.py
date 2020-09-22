# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。 
# 
#  例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 12
# 输出：5
#  
# 
#  示例 2： 
# 
#  输入：n = 13
# 输出：6 
# 
#  
# 
#  限制： 
# 
#  
#  1 <= n < 2^31 
#  
# 
#  注意：本题与主站 233 题相同：https://leetcode-cn.com/problems/number-of-digit-one/ 
#  Related Topics 数学


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countDigitOne(self, n: int) -> int:
        """
        将n分为三段：high，cur，low
        digit为cur所在位置的位数
        规律：
        当cur == 0：res += digit * high
        当cur == 1：res += digit * high + low + 1
        当1 < cur < 10:res += digit * high + digit
        """
        res, low, digit = 0, 0, 1
        high, cur = n // 10, n % 10
        while low != n:
            if cur == 0:
                res += digit * high
            elif cur == 1:
                res += digit * high + low + 1
            else:
                res += digit * high + digit
            cur = high % 10
            high //= 10
            digit *= 10
            low = n % digit
        return res
# leetcode submit region end(Prohibit modification and deletion)

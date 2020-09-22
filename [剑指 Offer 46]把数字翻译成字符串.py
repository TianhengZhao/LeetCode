# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可
# 能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi" 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= num < 231


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1
        num_str = str(num)
        # basecase
        tmp1, tmp2 = 1, 1
        for i in range(1, len(num_str)):
            cur = int(num_str[i - 1:i + 1])
            # 判断条件看前一数和当前数是否在[10,25]间
            if 10 <= cur <= 25:
                # 转移方程1
                tmp1, tmp2 = tmp2, tmp1 + tmp2
            else:
                # 转移方程2
                tmp1 = tmp2
        return tmp2

# leetcode submit region end(Prohibit modification and deletion)

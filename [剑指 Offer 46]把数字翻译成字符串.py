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
        num_str = str(num)
        # basecase
        tmp0, tmp1 = 1, 1
        for i in range(1, len(num_str)):
            cur = int(num_str[i - 1:i + 1])
            # 看前一数和当前数是否在[10,25]间
            if 10 <= cur <= 25:
                # cur可以翻译为字符，当前tmp为前两tmp的和
                tmp0, tmp1 = tmp1, tmp0 + tmp1
            else:
                # cur不能翻译为字符，和前一tmp数量相同
                tmp0 = tmp1
        return tmp1

# leetcode submit region end(Prohibit modification and deletion)

# 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。 
# 
#  （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。） 
# 
#  示例 1: 
# 
#  输入: N = 10
# 输出: 9
#  
# 
#  示例 2: 
# 
#  输入: N = 1234
# 输出: 1234
#  
# 
#  示例 3: 
# 
#  输入: N = 332
# 输出: 299
#  
# 
#  说明: N 是在 [0, 10^9] 范围内的一个整数。 
#  Related Topics 贪心算法 


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        str_n, j = str(N), -1
        for i in range(len(str_n) - 1):
            if str_n[i] > str_n[i + 1]:
                j = i
                # 1231,j在3的位置；1331，j在最左的3；
                while j > 0 and str_n[j] == str_n[j - 1]:
                    j -= 1
                break
        # 没有降序
        if j == -1:
            return N
        # 10...
        if str_n[j] == '1':
            return int('9' * (len(str_n) - 1))
        # j之前的高位
        high = str_n[:j] if j != 0 else '0'
        pivot = len(str_n) - j
        # 高位+j所在位置+j后位置
        return int(high) * 10 ** pivot + (int(str_n[j]) - 1) * 10 ** (pivot - 1) + int('9' * (pivot - 1))

# leetcode submit region end(Prohibit modification and deletion)

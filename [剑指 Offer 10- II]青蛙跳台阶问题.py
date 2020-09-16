# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。 
# 
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
# 示例 ：
# 输入：n = 7
# 输出：21
#  
# 
# 示例 ：
# 输入：n = 0
# 输出：1 
# 
#  提示：
#  0 <= n <= 100
#  Related Topics 递归


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numWays(self, n: int) -> int:
        """就是斐波那契问题"""
        tmp1, tmp2 = 1, 1
        for _ in range(2, n+1):
            tmp1, tmp2 = tmp2, tmp1+tmp2
        return tmp2 % 1000000007

# leetcode submit region end(Prohibit modification and deletion)

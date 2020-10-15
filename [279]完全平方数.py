# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。 
# 
#  示例 1: 
# 
#  输入: n = 12
# 输出: 3 
# 解释: 12 = 4 + 4 + 4. 
# 
#  示例 2: 
# 
#  输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9. 
#  Related Topics 广度优先搜索 数学 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def numSquares_ans(self, n: int) -> int:
        # 小于等于n的所有完全平方数
        sqrts = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]
        # 足够大的数
        max_num = 10000
        # dp[0]便于计算
        dp = [0] + [max_num for _ in range(n)]
        for i in range(1, n + 1):
            for sqrt in sqrts:
                if sqrt <= i:
                    dp[i] = min(dp[i], dp[i - sqrt] + 1)
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)

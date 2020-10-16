# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。 
# 
#  示例 1: 
# 
#  输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。 
# 
#  示例 2: 
# 
#  输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。 
# 
#  说明: 你可以假设 n 不小于 2 且不大于 58。 
#  Related Topics 数学 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(3, n + 1):
            for j in range(1, i // 2 + 1):
                # ！
                dp[i] = max(j * dp[i - j], dp[i], j * (i - j))
        return dp[-1]

# leetcode submit region end(Prohibit modification and deletion)

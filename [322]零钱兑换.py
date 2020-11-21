# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。 
# 
#  你可以认为每种硬币的数量是无限的。
#  示例 1： 
# 
#  
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1 
# 
#  示例 2： 
# 
#  
# 输入：coins = [2], amount = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：coins = [1], amount = 0
# 输出：0
#
# 
#  提示： 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 231 - 1 
#  0 <= amount <= 104 
#  
#  Related Topics 动态规划

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """动态规划
        dp[i]为金额i需要硬币的最小数量
        """
        if not amount:
            return 0
        # dp中的值amount+1相当于max_value
        dp = [0] + [amount + 1] * amount
        # 对于金额i
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                # 遍历每个比金额i小的硬币
                if i >= coins[j]:
                    # 是否算上该硬币
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return -1 if dp[-1] == amount + 1 else dp[-1]
# leetcode submit region end(Prohibit modification and deletion)

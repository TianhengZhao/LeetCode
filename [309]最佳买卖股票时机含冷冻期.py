# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。 
# 
#  设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）: 
# 
#  
#  你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
#  卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。 
#  
# 
#  示例: 
# 
#  输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出] 
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        length = len(prices)
        # 原dp为length*3二维数组，空间优化如下，dpi表示当天结束后会出现的三种状态
        # dp0表示持有股票，即当天买入股票，或之前买入今天未卖出
        # dp1表示不持有股票，即当天卖出股票，下一天为冷冻期
        # dp2表示不持有股票，即当天处于冷冻期或无动作，下一天可以买入可以无动作
        dp0, dp1, dp2 = -prices[0], 0, 0
        for i in range(1, length):
            # 暂存
            tmp0, tmp1, tmp2 = dp0, dp1, dp2
            dp0 = max(tmp2 - prices[i], tmp0)
            dp1 = tmp0 + prices[i]
            dp2 = max(tmp1, tmp2)
        return max(dp1, dp2)
# leetcode submit region end(Prohibit modification and deletion)

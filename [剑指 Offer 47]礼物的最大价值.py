# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直
# 到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？ 
# 
#  
# 
#  示例 1: 
# 
#  输入: 
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 12
# 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物 
# 
#  
# 
#  提示： 
# 
#  
#  0 < grid.length <= 200 
#  0 < grid[0].length <= 200 
#  
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 优化了空间，棋盘中对应位置的礼物最大值
        dp = [0] * n
        for i in range(m):
            # 初始化，每行第一列礼物价值
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = grid[i][j] + max(dp[j], dp[j - 1])
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)

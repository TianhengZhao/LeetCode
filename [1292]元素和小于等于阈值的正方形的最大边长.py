# 给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。 
# 
#  请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。 
#  
# 
#  示例 1：
# 
#  输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# 输出：2
# 解释：总和小于 4 的正方形的最大边长为 2
#
#  1 <= m, n <= 300 
#  m == mat.length 
#  n == mat[i].length 
#  0 <= mat[i][j] <= 10000 
#  0 <= threshold <= 10^5 
#  
#  Related Topics 数组 二分查找

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """注意dp[i][j]和tmp中， 行列索引的计算"""

    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """二维前缀和+从大到小查找"""
        m, n = len(mat), len(mat[0])
        # 第0行和第0列为辅助行、列，便于计算前缀和
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = mat[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
        # 边长由大到小计算方形之和是否 <= threshold
        for length in range(min(m, n), -1, -1):
            # 右下角开始计算
            for i in range(m, length - 1, -1):
                for j in range(n, length - 1, -1):
                    # 由前缀和计算原矩阵某区域元素和（减去多余部分，加会多减掉的重叠部分）
                    tmp = dp[i][j] - dp[i - length][j] - dp[i][j - length] + dp[i - length][j - length]
                    if tmp <= threshold:
                        return length
        return 0

    def maxSideLength_bin(self, mat: List[List[int]], threshold: int) -> int:
        """二维前缀和+二分查找"""
        m, n = len(mat), len(mat[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]

        left, right, res = 1, min(m, n), 0
        # 在查找最大正方形边长时，使用二分查找
        while left <= right:
            mid = (left + right) // 2
            # 记录该边长是否有元素和 <= threshold的情况
            flag = False
            for i in range(mid, m + 1):
                for j in range(mid, n + 1):
                    tmp = dp[i][j] - dp[i - mid][j] - dp[i][j - mid] + dp[i - mid][j - mid]
                    if tmp <= threshold:
                        flag = True
            # 当前边长满足条件，是否有更大边长
            if flag:
                res = mid
                left = mid + 1
            # 当前边长不满足，看较小边长是否满足条件
            else:
                right = mid - 1
        return res
        
# leetcode submit region end(Prohibit modification and deletion)

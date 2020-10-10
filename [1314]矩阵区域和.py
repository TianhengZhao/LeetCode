# 给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 ma
# t[r][c] 的和：
#  i - K <= r <= i + K, j - K <= c <= j + K 
#  (r, c) 在矩阵内。
# 
#  示例 1： 
# 
#  输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]
#  
# 
#  示例 2： 
# 
#  输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
# 输出：[[45,45,45],[45,45,45],[45,45,45]]
#
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n, K <= 100 
#  1 <= mat[i][j] <= 100 
#  
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 计算前缀和
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = mat[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
        if K + 1 >= max(m, n):
            return [[dp[m][n]] * n for _ in range(m)]
        ans = [[0] * n for _ in range(m)]
        # r_row, r_col为dp子区域最右下位置
        # l_row+1, l_col+1为dp子区域最左上位置
        for i in range(m):
            for j in range(n):
                # 计算dp子区域边界值
                r_row, r_col = min(i + K + 1, m), min(j + K + 1, n)
                l_row, l_col = max(i - K, 0), max(j - K, 0)
                ans[i][j] = dp[r_row][r_col] - dp[l_row][r_col] - dp[r_row][l_col] + dp[l_row][l_col]
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)

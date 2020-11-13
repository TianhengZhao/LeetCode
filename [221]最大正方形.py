# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：
# matrix = [["1","0","1","0","0"],
#           ["1","0","1","1","1"],
#           ["1","1","1","1","1"],
#           ["1","0","0","1","0"]]
# 
# 输出：4 
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        """空间优化1
        二维dp化成两个一维数组"""
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp1 = dp2 = [0] * (n + 1)
        max_len = 0
        for i in range(m):
            for j in range(1, n + 1):
                if matrix[i][j - 1] == '1':
                    dp2[j] = min(dp2[j - 1], dp1[j - 1], dp1[j]) + 1
                else:
                    dp2[j] = 0
            max_len = max(max(dp2), max_len)
            # 这里用dp2[:]浅拷贝一个副本给dp1， 若dp1=dp2赋的是指针
            dp1 = dp2[:]
        return max_len ** 2

    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        """空间优化2"""
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)
        # 用pre暂存原二维dp中该位置左上位置值
        max_len, pre = 0, 0
        for i in range(m):
            for j in range(1, n + 1):
                # 记录dp[j]，之后赋给pre，留给j+1用
                tmp = dp[j]
                if matrix[i][j - 1] == '1':
                    # j左侧，上面，左上的最小值
                    dp[j] = min(pre, dp[j - 1], dp[j]) + 1
                else:
                    # 用0覆盖旧值
                    dp[j] = 0
                pre = tmp
            # 要进行下一行dp，pre为0
            pre = 0
            max_len = max(max(dp), max_len)
        return max_len ** 2

# leetcode submit region end(Prohibit modification and deletion)

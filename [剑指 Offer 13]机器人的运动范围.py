# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一
# 格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但
# 它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？ 
# 
#  
# 
#  示例 1： 
# 
#  输入：m = 2, n = 3, k = 1
# 输出：3
#  
# 
#  示例 2： 
# 
#  输入：m = 3, n = 1, k = 0
# 输出：1
#  
# 
#  提示： 
# 
#  
#  1 <= n,m <= 100 
#  0 <= k <= 20


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/
    写出每个格子行列的和，找规律
    小于k的格子排列是斜边平行于主对角线的等腰直角三角形
    向右向下查找即可
    """
    def sum(self, x):
        res = 0
        while x:
            res += x % 10
            x //= 10
        return res

    def movingCount_1(self, m: int, n: int, k: int) -> int:
        """
        迭代
        时间复杂度O（MN）
        无论k多小都要遍历整个格子数组
        """
        visited = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                # 左格子或者上格子被访问过，且位数和<k，将该格子加入已访问
                if ((i - 1, j) in visited or (i, j - 1) in visited) and self.sum(i) + self.sum(j) <= k:
                    visited.add((i, j))
        return len(visited)

    def movingCount_2(self, m: int, n: int, k: int) -> int:
        """
        递归
        *可优化求位数和的方法
        """
        visited = set()

        def dfs(row, col):
            # 返回0的情况：1.位数和大于k 2.已被访问过 3.超过右边界 4.超过下边界
            if self.sum(row) + self.sum(col) > k or (row, col) in visited or row == m or col == n:
                return 0
            visited.add((row, col))
            return 1 + dfs(row + 1, col) + dfs(row, col + 1)

        return dfs(0, 0)
# leetcode submit region end(Prohibit modification and deletion)




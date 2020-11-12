# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] 的值为 '0' 或 '1' 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from typing import List


class Solution:
    def numIslandsAns(self, grid: List[List[str]]) -> int:
        """
        bfs
        """
        # m行n列的矩阵
        m, n = len(grid), len(grid[0])
        # 岛屿个数
        res = 0
        # 存放该岛屿内岛的位置
        neigh = deque()
        for i in range(m):
            for j in range(n):
                # 进入一个岛屿区域，将该岛屿区域所有1化为0，下一次进入此if就是下一个岛屿
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = '0'
                    neigh.append([i, j])
                    # 附近是否还有岛
                    while neigh:
                        # 每个岛的四周都要遍历是否有岛，有则入队，置0代表已访问过
                        row, col = neigh.popleft()
                        for x, y in [[row - 1, col], [row, col - 1], [row + 1, col], [row, col + 1]]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                                neigh.append([x, y])
                                grid[x][y] = '0'
        return res

    def numIslandsAns2(self, grid: List[List[str]]) -> int:
        """
        递归dfs
        找到岛屿起始位置，从起始位置开始dfs把相邻1都置0即可
        """
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, row, col):
        m, n = len(grid), len(grid[0])
        grid[row][col] = '0'
        for x, y in [[row + 1, col], [row, col - 1], [row - 1, col], [row, col + 1]]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                self.dfs(grid, x, y)
# leetcode submit region end(Prohibit modification and deletion)

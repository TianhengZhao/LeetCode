# 给定一个 n × n 的二维矩阵表示一个图像。 
# 
#  将图像顺时针旋转 90 度。 
# 
#  说明： 
# 
#  你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。 
# 
#  示例 1: 
# 
#  给定 matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# 
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
#  
# 
#  示例 2: 
# 
#  给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ], 
# 
# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        见笔记
        """
        n = len(matrix)
        layers = (n + 1) // 2
        for layer in range(layers):
            for i in range(layer, n - layer - 1):
                row, col = layer, i
                tmp = matrix[row][col]
                for k in range(3):
                    matrix[row][col] = matrix[n - 1 - col][row]
                    row, col = n - 1 - col, row
                matrix[row][col] = tmp
# leetcode submit region end(Prohibit modification and deletion)

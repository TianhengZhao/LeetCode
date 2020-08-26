# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  限制： 
# 
#  
#  0 <= matrix.length <= 100 
#  0 <= matrix[i].length <= 100 
#  
# 
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/ 
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        由外向里逐层遍历
        每次while写入一层的一条边
        注：也可以一次while直接写入一层的四条边
        """
        if not matrix:
            return []
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        pos = [0, 0]
        res = []

        # 注意结束条件。之前就写错了
        while left <= right and top <= bottom:
            if pos == [top, left]:
                res += matrix[top][left:right+1]
                top += 1
                pos = [top, right]
            elif pos == [top, right]:
                for i in range(top, bottom+1):
                    res.append(matrix[i][right])
                right -= 1
                pos = [bottom, right]
            elif pos == [bottom, right]:
                res += list(reversed(matrix[bottom][left:right+1]))
                bottom -= 1
                pos = [bottom, left]
            else:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
                pos = [top, left]

        return res
# leetcode submit region end(Prohibit modification and deletion)

# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。 
# 
#  
# 
#  在杨辉三角中，每个数是它左上方和右上方的数的和。 
# 
#  示例: 
# 
#  输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ] 
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            tmp = []
            for j in range(len(res[i - 1]) - 1):
                tmp.append(res[i - 1][j] + res[i - 1][j + 1])
            res.append([1] + tmp + [1])
        return res
# leetcode submit region end(Prohibit modification and deletion)

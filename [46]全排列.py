# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if not length:
            return []
        used = [False for _ in range(length)]
        self.res = []
        self.backtrack(nums, length, 0, used, [])
        return self.res

    def backtrack(self, nums, length, depth, used, path):
        # 递归出口
        if depth == length:
            # 注意此处不可res.append(path),最后输出均为[]，因为最后path为[]
            # 应该做值的拷贝
            self.res.append(path[:])
            return
        # 每次递归都要遍历一次nums
        for i in range(length):
            # 对于未被访问过的nums[i]
            if not used[i]:
                # 做选择
                # 选择该nums[i]为当前路径
                used[i] = True
                path.append(nums[i])
                # 向下一深度递归
                self.backtrack(nums, length, depth + 1, used, path)
                # 回溯，撤销选择
                used[i] = False
                path.pop()
# leetcode submit region end(Prohibit modification and deletion)

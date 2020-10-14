# 给定一个可包含重复数字的序列，返回所有不重复的全排列。 
# 
#  示例: 
# 
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ] 
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if not length:
            return []
        # 排序，相同的数字排在一起
        nums.sort()
        self.res = []
        used = [False for _ in range(length)]
        self.backtrack(nums, 0, used, length, [])
        return self.res

    def backtrack(self, nums, depth, used, length, path):
        if depth == length:
            self.res.append(path[:])
            return
        for i in range(length):
            if used[i]:
                continue
            # 如果此数字和前一数字相等，且前一数字在此分支未使用过，则剪枝，因为此分支重复了
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtrack(nums, depth + 1, used, length, path)
            used[i] = False
            path.pop()
# leetcode submit region end(Prohibit modification and deletion)

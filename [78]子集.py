# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  示例: 
# 
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ] 
#  Related Topics 位运算 数组 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """回溯"""
        if not nums:
            return []
        res = [[]]
        self.backtrack(nums, 0, [], res)
        return res

    def backtrack(self, nums, index, cur, res):
        # 无重复元素，i从index开始遍历
        for i in range(index, len(nums)):
            # 中间结果放入res
            res.append(cur + [nums[i]])
            self.backtrack(nums, i + 1, cur + [nums[i]], res)
# leetcode submit region end(Prohibit modification and deletion)

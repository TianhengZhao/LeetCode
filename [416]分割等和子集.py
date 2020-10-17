# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  注意: 
# 
#  
#  每个数组中的元素不会超过 100 
#  数组的大小不会超过 200 
#  
# 
#  示例 1: 
# 
#  输入: [1, 5, 11, 5]
# 
# 输出: true
# 
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
#
# 
#  示例 2: 
# 
#  输入: [1, 2, 3, 5]
# 
# 输出: false
# 
# 解释: 数组不能分割成两个元素和相等的子集.
#  
# 
#  
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    0-1背包问题。从数组中选一些数字，和为整个数组元素和的一半
    """
    def canPartition_ans(self, nums: List[int]) -> bool:
        # 直接返回false的情况
        # 1.数组长小于2
        length = len(nums)
        if length < 2:
            return False
        total = sum(nums)
        target = total // 2
        # 2.元素和为奇数  3.元素和的一半小于nums中最大值(可以等于)
        if total % 2 or target < max(nums):
            return False
        # 二维dp，n行target+1列，dp[i][j]表示数组中0-i几个位置，是否有若干数的和为j
        dp = [[False] * (target + 1) for _ in range(length)]
        # basecase
        for i in range(length):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1, length):
            for j in range(1, target + 1):
                if j >= nums[i]:
                    # 考虑把nums[i]加进来的情况
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    # 不用加nums[i]
                    dp[i][j] = dp[i - 1][j]
        return dp[length - 1][target]
# leetcode submit region end(Prohibit modification and deletion)

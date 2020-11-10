# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
#  Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """动态规划 暴力法 超时"""
        dp = [1] * len(nums)
        res = nums[0]
        for i in range(len(nums)):
            for j in range(i + 1):
                dp[j] *= nums[i]
                res = max(dp[j], res)
        return res

    def maxProductAns(self, nums: List[int]) -> int:
        """
        动态规划 时间复杂度O(n)
        用pre_min记录最小值，尤其是奇数个负数的时候，这样当下个数是负数，得到最大值
        这种情况在只记录pre_max的情况下是会被忽略导致错误的
        """
        res, pre_max, pre_min = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_max = max(pre_max * nums[i], nums[i], pre_min * nums[i])
            cur_min = min(pre_max * nums[i], nums[i], pre_min * nums[i])
            res = max(cur_max, res)
            pre_max, pre_min = cur_max, cur_min
        return res
    # leetcode submit region end(Prohibit modification and deletion)

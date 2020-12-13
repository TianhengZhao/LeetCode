# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。 
# 
#  要求时间复杂度为O(n)。 
# 
#  
# 
#  示例1: 
# 
#  输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^5 
#  -100 <= arr[i] <= 100 
#  
# 
#  注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/ 
# 
#  
#  Related Topics 分治算法 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        """
        dp[i]中存储 以nums[i]为最后一个元素 的连续数组的最大和
        """
        # basecase
        res = dp = nums[0]
        for i in range(1, len(nums)):
            dp = max(nums[i], nums[i] + dp)
            res = max(dp, res)
        return res

# leetcode submit region end(Prohibit modification and deletion)

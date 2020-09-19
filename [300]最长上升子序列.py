# 给定一个无序的整数数组，找到其中最长上升子序列的长度。 
# 
#  示例: 
# 
#  输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。 
# 
#  说明: 
# 
#  
#  可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。 
#  你算法的时间复杂度应该为 O(n2) 。 
#  
# 
#  进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗? 不能
#  Related Topics 二分查找 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        时间复杂度O（n^2）
        i从头到尾遍历nums，对于每个i，从0遍历到i-1
        """
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # dp[i]为 nums[i]作为升序序列最后一位数时 的最长序列长度
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        
# leetcode submit region end(Prohibit modification and deletion)

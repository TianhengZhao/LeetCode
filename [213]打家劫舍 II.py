# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋
# 装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。 
# 
#  给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。 
# 
#  示例 1: 
# 
#  输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#  
# 
#  示例 2: 
# 
#  输入: [1,2,3,1]
# 输出: 4
# 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。 
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def rob_ans(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        # 去掉头或尾，将环变为单链
        return max(self.helper(nums[:length - 1], length - 1), self.helper(nums[1:], length - 1))

    def helper(self, nums, length):
        if not length:
            return 0
        if length <= 2:
            return max(nums)
        pos1, pos2 = nums[0], max(nums[0], nums[1])
        for i in range(2, length):
            pos1, pos2 = pos2, max(pos2, pos1 + nums[i])
        return pos2

# leetcode submit region end(Prohibit modification and deletion)

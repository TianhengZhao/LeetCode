# 统计一个数字在排序数组中出现的次数。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2 
# 
#  示例 2: 
# 
#  输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0 
# 
#  
# 
#  限制： 
# 
#  0 <= 数组长度 <= 50000 
# 
#  
# 
#  注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-
# position-of-element-in-sorted-array/ 
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def search_ans(self, nums: List[int], target: int) -> int:
        """二分查找"""
        # 若target-1不存在，返回的left为target最左侧的值的位置
        return self.helper(nums, target) - self.helper(nums, target-1)

    def helper(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left+(right-left)//2
            # 值相同时，right为最右的相同值
            if target >= nums[mid]:
                left = mid+1
            else:
                right = mid-1
        # left为右边界，target最右侧值的位置+1
        return left

# leetcode submit region end(Prohibit modification and deletion)

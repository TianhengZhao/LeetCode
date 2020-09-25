# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出
# 这个数字。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [0,1,3]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [0,1,2,3,4,5,6,7,9]
# 输出: 8 
# 
#  
# 
#  限制： 
# 
#  1 <= 数组长度 <= 10000 
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """二分法"""
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] ^ 1
        if len(nums) == nums[-1] + 1:
            return nums[-1] + 1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # 计算距离
            if nums[right] - nums[mid] > right - mid:
                left = mid + 1
            else:
                right = mid
        return nums[right] - 1

    def missingNumber_ans(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # 判断位置上的数
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left
# leetcode submit region end(Prohibit modification and deletion)

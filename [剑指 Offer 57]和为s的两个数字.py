# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [2,7,11,15], target = 9
# 输出：[2,7] 或者 [7,2]
#  
# 
#  示例 2： 
# 
#  输入：nums = [10,26,30,31,47,60], target = 40
# 输出：[10,30] 或者 [30,10]
#  
# 
#  
# 
#  限制： 
# 
#  
#  1 <= nums.length <= 10^5 
#  1 <= nums[i] <= 10^6


# leetcode submit region begin(Prohibit modification and deletion)
from typing import  List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """两个指针分别从头尾向中间移动"""
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [nums[left], nums[right]]
        return []
# leetcode submit region end(Prohibit modification and deletion)

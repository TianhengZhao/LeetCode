# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。 
# 
#  
# 
#  示例： 
# 
#  输入：nums = [1,2,3,4]
# 输出：[1,3,2,4] 
# 注：[3,1,2,4] 也是正确的答案之一。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 50000 
#  1 <= nums[i] <= 10000 
#


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        """
        类似于快排思想
        左指针从左找出偶数
        右指针从右找出奇数
        左右指针交换
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            while nums[left] & 1 == 1 and left < right:
                left += 1
            while nums[right] & 1 == 0 and right > left:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums
# leetcode submit region end(Prohibit modification and deletion)

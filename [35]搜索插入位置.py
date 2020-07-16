# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。 
# 
#  你可以假设数组中无重复元素。 
# 
#  示例 1: 
# 
#  输入: [1,3,5,6], 5
# 输出: 2
#  
#  Related Topics 数组 二分查找 



# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def searchInsert_mine(self, nums: List[int], target: int) -> int:
        """
        二分查找
        O（logn）
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2  # 防止溢出
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return left   # 此处返回left即可

    def searchInsert_other(self, nums: List[int], target: int) -> int:
        """
        使用内置函数
        将target加入列表后排序，再找出target的索引
        O(nlogn)
        """
        nums.append(target)
        nums.sort()
        return nums.index(target)

# leetcode submit region end(Prohibit modification and deletion)

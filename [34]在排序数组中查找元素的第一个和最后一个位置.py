# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 
# 
#  你的算法时间复杂度必须是 O(log n) 级别。 
# 
#  如果数组中不存在目标值，返回 [-1, -1]。 
# 
#  示例 1: 
# 
#  输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4] 
# 
#  示例 2: 
# 
#  输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1] 
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def searchRange_ans(self, nums: List[int], target: int) -> List[int]:
        """
        用二分查找分别找到首尾位置
        """
        if not nums:
            return [-1, -1]
        first_pos = self.findFirstPos(nums, target)
        if first_pos == -1:
            return [-1, -1]
        last_pos = self.findLastPos(nums, target)
        return [first_pos, last_pos]

    def findFirstPos(self, nums, target):
        """找到最左侧的target"""
        left, right = 0, len(nums) - 1
        # 不能取等 会死循环
        while left < right:
            mid = left + (right - left) // 2
            # 目标 > mid位置值，所有目标值在[mid+1, right]内
            if target > nums[mid]:
                left = mid + 1
            # 目标 <= mid位置值，最左的目标在[left, mid]中
            else:
                right = mid
        # 最后一次while时，一定只有两个数了，mid取地板，left = mid = right-1
        # 若target > nums[mid], left = mid + 1 = right
        # 若target <= nums[mid], right = mid = left
        if nums[left] == target:
            return left
        return -1

    def findLastPos(self, nums, target):
        """ 找最右侧target """
        left, right = 0, len(nums) - 1
        while left < right:
            # 取天棚！
            mid = left + (right - left) // 2 + 1
            # 目标 < mid位置值，所有目标值在[left, mid-1]内
            if target < nums[mid] :
                right = mid - 1
            # 目标 >= mid位置值，最右的目标在[mid， right]中
            else:
                left = mid
        return left


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        在target几乎与数组等长时，时间复杂度退化到O(N)
        """
        length = len(nums)
        if not length:
            return [-1, -1]
        left, right = 0, length - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                start = end = mid
                # 找到之后，从该点依次向左右找相等的值
                while start - 1 >= 0 and nums[start] == nums[start - 1]:
                    start -= 1
                while end + 1 < length and nums[end] == nums[end + 1]:
                    end += 1
                return [start, end]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1, -1]
# leetcode submit region end(Prohibit modification and deletion)

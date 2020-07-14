# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。 
# 
#  不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。 

#  
#  Related Topics 数组 双指针 



# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def removeDuplicates_mine(self, nums: List[int]) -> int:
        """
        使用双指针方法
        时间复杂度O（n）
        """
        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[length] = nums[i]
                length += 1
        return length

    def removeDuplicates_other(self, nums: List[int]) -> int:
        """
        从后往前遍历
        双指针，若前后两元素相同，删除一个
        """
        a = len(nums)
        for i in range(len(nums)):
            if (nums[a - i - 1]) == (nums[a - i - 2]) and (i < a - 1):
                nums.pop(a - i - 1)
            else:
                continue
        return len(nums)


# leetcode submit region end(Prohibit modification and deletion)

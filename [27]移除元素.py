# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。 
# 
#  不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。 
# 
#  元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。 
# 
#  
# 
#  示例 1: 
# 
#  给定 nums = [3,2,2,3], val = 3,
# 
# 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
# 
# 你不需要考虑数组中超出新长度后面的元素。
#  

#  Related Topics 数组 双指针 



# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def removeElement_mine1(self, nums: List[int], val: int) -> int:
        """
        从后向前遍历
        删除数组中与val相同的元素
        """
        length = len(nums)
        for i in range(length - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)

    def removeElement_other(self, nums: List[int], val: int) -> int:
        """
        双指针方法
        """
        i = 0
        for j in range(0, len(nums)):
            # 如果nums[j]不等于val, 则将nums[j]赋值给nums[i]即可, i自增
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
# leetcode submit region end(Prohibit modification and deletion)

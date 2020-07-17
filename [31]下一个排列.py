# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。 
# 
#  如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。 
# 
#  必须原地修改，只允许使用额外常数空间。 
# 
#  以下是一些例子，输入位于左侧列，其相应输出位于右侧列。 
# 1,2,3 → 1,3,2 
# 3,2,1 → 1,2,3 
# 1,1,5 → 1,5,1 
#  Related Topics 数组 


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def nextPermutation_other(self, nums: List[int]) -> None:
        """
        从右向左找出第一个nums[i] > nums[i - 1]的位置i-1，记为pos
        从右向左找出第一个比nums[pos]大的数，并与其交换
        将pos右的序列按递增排序（原为递减排序）
        """
        def reverse(start, end):
            """将原序列逆序"""
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        if len(nums) > 1:
            pos = -1
            for i in range(len(nums) - 1, 0, -1):
                if nums[i] > nums[i - 1]:
                    pos = i - 1
                    break
            if pos != -1:
                for i in range(len(nums) - 1, pos, -1):
                    if nums[i] > nums[pos]:
                        nums[i], nums[pos] = nums[pos], nums[i]
                        break
                reverse(pos + 1, len(nums) - 1)
            else:
                nums.sort()

# leetcode submit region end(Prohibit modification and deletion)

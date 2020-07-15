# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例： 
# 
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  
#  Related Topics 数组 双指针 



# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeSum_other(self, nums: List[int]) -> List[List[int]]:
        """
        先对列表排序
        固定一个元素i
        双指针left，right分别指向i右侧的头和尾
        判断i，left，right位置元素和是否为0
        大于0，左移right，反之亦然
        移动i和指针时跳过重复元素
        """
        if len(nums) <= 2:
            return []
        nums.sort()
        res = []
        length = len(nums)
        for i in range(length-2):
            if nums[i] > 0:
                return res
            # 若i处为重复值，跳过
            if i > 0 and nums[i] == nums[i-1]:
                continue
            right = length-1
            left = i+1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # 跳过重复元素，否则结果会出错
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)

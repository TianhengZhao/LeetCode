# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。 
# 
#  此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。 
# 
#  注意: 
# 不能使用代码库中的排序函数来解决这道题。 
# 
#  示例: 
# 
#  输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2] 
# 
#  进阶： 
# 
#  
#  一个直观的解决方案是使用计数排序的两趟扫描算法。 
#  首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。 
#  你能想出一个仅使用常数空间的一趟扫描算法吗？ 
#  
#  Related Topics 排序 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """遍历两次，第一次计数，第二次更新根据计数更新nums"""
        red, white, blue = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                red += 1
            elif nums[i] == 1:
                white += 1
            else:
                blue += 1
        for i in range(len(nums)):
            if i < red:
                nums[i] = 0
            elif i < red + white:
                nums[i] = 1
            else:
                nums[i] = 2

    def sortColorsAns(self, nums: List[int]) -> None:
        """
        快排的思想
        """
        # [0,left)均为0， [left, i)均为1， [right, len(nums)]均为2
        left = i = 0
        right = len(nums)
        while i < right:
            if nums[i] == 0:
                # i遇到0，和left交换，保证left左侧均为0
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 1:
                # 遇到1，加1。i左侧是排好序的0和1， i到two未排序，two到结尾均为2
                i += 1
            else:
                # 此处right不可初始化为len(nums)-1，然后先交换，right再减1，会出错
                # 即此处right该为闭区间 不该为开，否则由于while循环是小于，未比较最后一个值，提前结束
                right -= 1
                nums[right], nums[i] = nums[i], nums[right]

# leetcode submit region end(Prohibit modification and deletion)

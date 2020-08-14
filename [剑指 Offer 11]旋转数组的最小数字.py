# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2
# ] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。 
# 
#  示例 1： 
# 
#  输入：[3,4,5,1,2]
# 输出：1
#  
# 
#  示例 2： 
# 
#  输入：[2,2,2,0,1]
# 输出：0
#  
# 
#  注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sor
# ted-array-ii/ 
#  Related Topics 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def minArray_1(self, numbers: List[int]) -> int:
        """找第一个逆序"""
        for i in range(len(numbers) - 1):
            if numbers[i + 1] < numbers[i]:
                return numbers[i + 1]
        return numbers[0]

    def minArray_answer(self, numbers: List[int]) -> int:
        """
        二分查找的思想
        每次都将mid和right进行比较
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = left + (right - left) // 2
            # mid右侧是正常升序，最小值在mid左侧
            if numbers[mid] < numbers[right]:
                right = mid
            # mid右侧出现逆序，最小值在mid右侧
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            # mid和right处值相等，有可能连续，有可能分别在头和尾
            else:
                right -= 1
        return numbers[left]

# leetcode submit region end(Prohibit modification and deletion)

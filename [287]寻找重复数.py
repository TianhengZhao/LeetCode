# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出
# 这个重复的数。 
# 
#  示例 1: 
# 
#  输入: [1,3,4,2,2]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [3,1,3,4,2]
# 输出: 3
#  
# 
#  说明： 
# 
#  
#  不能更改原数组（假设数组是只读的）。 
#  只能使用额外的 O(1) 的空间。 
#  时间复杂度小于 O(n2) 。 
#  数组中只有一个重复的数字，但它可能不止重复出现一次。 
#  
#  Related Topics 数组 双指针 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        时间复杂度O（nlogn）空间复杂度O（n）
        对1到n进行二分
        数组是无序的 不是对数组二分
        还有时间复杂度O（n）的方法
        """
        # nums中数值的取值范围
        left, right = 1, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            # 计算小于等于mid的数值个数
            for num in nums:
                if num <= mid:
                    count += 1
            # 左侧没有重复数值
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        return left
# leetcode submit region end(Prohibit modification and deletion)

# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。 
# 
#  你找到的子数组应是最短的，请输出它的长度。 
# 
#  示例 1: 
# 
#  
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#  
# 
#  说明 : 
# 
#  
#  输入的数组长度范围在 [1, 10,000]。 
#  输入的数组可能包含重复元素 ，所以升序的意思是<=。 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findUnsortedSubarraySort(self, nums: List[int]) -> int:
        """
        排序，比较不同
        时间复杂度O（nlogn）
        空间复杂度O（n）
        """
        cp, length = sorted(nums), len(nums)
        tmp, res = length, 0
        for i in range(length):
            if nums[i] != cp[i]:
                tmp = min(tmp, i)
                res = i - tmp + 1
        return res

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        时间复杂度 O(n)
        空间复杂度 O(1)
        """
        length = len(nums)
        min_val, max_val = max(nums), min(nums)
        flag = False
        # 从左往右，遇到逆序，flag置位true，找此后出现的最小元素min_val，即为子序列中最左元素
        for i in range(length - 1):
            if nums[i] > nums[i + 1]:
                flag = True
            if flag:
                min_val = min(nums[i + 1], min_val)
        flag = False
        # 同上，从右往左找max_val，子序列最右元素
        for i in range(length - 1, 0, -1):
            if nums[i - 1] > nums[i]:
                flag = True
            if flag:
                max_val = max(nums[i - 1], max_val)
        left, right = 0, 0
        # 从左往右，找min_val本应在的位置
        for i in range(length):
            if min_val < nums[i]:
                left = i
                break
        # 同上，从右往左找max_val本应在的位置
        for i in range(length - 1, -1, -1):
            if nums[i] < max_val:
                right = i
                break
        if right - left <= 0:
            return 0
        return right - left + 1

    # leetcode submit region end(Prohibit modification and deletion)

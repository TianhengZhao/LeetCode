# 给你一个整数数组 nums，请你将该数组升序排列。
#  示例 1： 
# 
#  输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#  
# 
#  示例 2： 
# 
#  输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 50000 
#  -50000 <= nums[i] <= 50000


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
import random


class Solution:
    def mergeSort(self, nums: List[int]) -> List[int]:
        """归并排序 O（nlogn）"""
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        if i < len(left):
            res += left[i:]
        else:
            res += right[j:]
        return res

    def quickSort(self, nums: List[int]) -> List[int]:
        """快速排序  O（nlogn）"""
        return self.quick(nums, 0, len(nums) - 1)

    def quick(self, nums, left, right):
        if left >= right:
            return nums
        # 随机选择作为基准的数 若选择最左或最右在逆序或正序时会很慢
        rand = random.randint(left, right)
        # 将基准数放在最左位置
        nums[rand], nums[left] = nums[left], nums[rand]
        pivot = left
        # 存储初始的左右指针值
        left_p, right_p = left, right
        while left < right:
            # 先对右侧while
            while left < right and nums[right] > nums[pivot]:
                right -= 1
            while left < right and nums[left] <= nums[pivot]:
                left += 1
            nums[left], nums[right] = nums[right], nums[left]
        nums[pivot], nums[right] = nums[right], nums[pivot]
        self.quick(nums, left_p, right - 1)
        self.quick(nums, right + 1, right_p)
        return nums

    def heapArray(self, nums):
        """堆排序 O（nlogn）"""
        length = len(nums)
        # 建堆
        for i in range(length // 2, -1, -1):
            self.sink(nums, i, n)
        # 将最大值和堆最右下元素交换后，重新排序
        for i in range(length - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.sink(nums, 0, i)
        return nums

    def sink(self, nums, start, end):
        target = nums[start]
        pos = start
        # 左子节点
        childpos = pos * 2 + 1
        while childpos < end:
            # 右子节点
            rightpos = childpos + 1
            if rightpos < end and nums[rightpos] >= nums[childpos]:
                # 现在childpos变成子节点中最大的那个
                childpos = rightpos
            if target < nums[childpos]:
                # 较大的子节点取代父节点
                nums[pos] = nums[childpos]
                # 原target现在的位置
                pos = childpos
                # childpos变成target新的左子节点
                childpos = pos * 2 + 1
            else:
                # 父节点都比子节点大，已成为大根堆
                break
        nums[pos] = target

# leetcode submit region end(Prohibit modification and deletion)

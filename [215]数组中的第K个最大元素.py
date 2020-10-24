# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 
# 
#  示例 1: 
# 
#  输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#  
# 
#  示例 2: 
# 
#  输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4 
# 
#  说明: 
# 
#  你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。 
#  Related Topics 堆 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
import random


class Solution:
    def findKthLargestQuick(self, nums: List[int], k: int) -> int:
        """
        利用快排的思想，每次partition后nums[random_index]都会到达它的最终位置
        """
        length = len(nums)
        target = length - k
        left, right = 0, length - 1
        while left <= right:
            index = self.partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index > target:
                right = index - 1
            else:
                left = index + 1

    def partition(self, nums, left, right):
        random_index = random.randint(left, right)
        nums[left], nums[random_index] = nums[random_index], nums[left]
        pivot = nums[left]
        i, j = left, right
        while i < j:
            # 先右，因为停下时一定nums[j]<=nums[left]
            while i < j and nums[j] > pivot:
                j -= 1
            while i < j and nums[i] <= pivot:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[j], nums[left] = nums[left], nums[j]
        return j

    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        """堆排序，大根堆，删k-1个堆顶，取第k个堆顶"""
        length = len(nums)
        # 建堆
        for i in range(length // 2 - 1, -1, -1):
            self.sink(nums, i, length)
        for i in range(k - 1):
            nums[0], nums[length - i - 1] = nums[length - i - 1], nums[0]
            self.sink(nums, 0, length - i - 1)
        return nums[0]

    def sink(self, nums, start, end):
        parent, target = start, nums[start]
        child = start * 2 + 1
        while child < end:
            right = child + 1
            # 别忘了判断right是否出界
            if right < end and nums[right] >= nums[child]:
                child = right
            # target从顶下沉，所以每次都是和target比
            if nums[child] > target:
                # 将较大的子节点移到父亲位置
                # 而后应该将父亲元素target移到子节点位置，不过没有必要，等到最后再移到
                nums[parent] = nums[child]
                parent = child
                child = parent * 2 + 1
            else:
                break
        # target放到其最终位置
        nums[parent] = target

# leetcode submit region end(Prohibit modification and deletion)

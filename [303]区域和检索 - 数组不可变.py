# 给定一个整数数组 nums，求出数组从索引 i 到 j (i ≤ j) 范围内元素的总和，包含 i, j 两点。 
# 
#  示例： 
# 
#  给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3 
# 
#  说明: 
# 
#  
#  你可以假设数组不可变。 
#  会多次调用 sumRange 方法。 
#  
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class NumArray_ans:

    def __init__(self, nums: List[int]):
        """设置缓存"""
        if nums:
            self.res = [nums[0]]
            # res[i]记录nums[0]到nums[i]的累加和
            for i in range(1, len(nums)):
                self.res.append(nums[i] + self.res[i - 1])
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return self.res[j] if i == 0 else self.res[j] - self.res[i - 1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# leetcode submit region end(Prohibit modification and deletion)

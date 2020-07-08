# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
#
#  Related Topics 数组 哈希表 
#


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def twoSum_mine(self, nums: List[int], target: int) -> List[int]:
        """
        暴力解法
        时间复杂度：O(n^2)
        空间复杂度：O(1)
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        第一次迭代遍历nums中后lengh-1个元素
        第二次判断target - nums[i]是否出现在i之前
        """
        lens = len(nums)
        j = -1
        for i in range(1, lens):
            temp = nums[:i]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                break
        if j >= 0:
            return [j, i]

    def twoSum_hashmap(self, nums: List[int], target: int) -> List[int]:
        """
        哈希表
        在第一次迭代中，将每个元素的值和它的索引添加到哈希表中。
        在第二次迭代中，判断每个元素所对应的目标元素（target - nums[i]）是否存在于哈希表中。
        """
        hashmap = {}
        for i, n in enumerate(nums):
            if target - n in hashmap:
                return [hashmap.get(target - n), i]
            hashmap[n] = i


        
# leetcode submit region end(Prohibit modification and deletion)

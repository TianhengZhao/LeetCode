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

    def twoSum_hashmap(self, nums: List[int], target: int) -> List[int]:
        """
        哈希表
        对于每个nums[i]，判断（target - nums[i]）是否存在于哈希表中，若存在，返回
        否则将nums[i]存入哈希表
        """
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i
        return []


        
# leetcode submit region end(Prohibit modification and deletion)

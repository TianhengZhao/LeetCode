# 给定一个范围在 1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。 
# 
#  找到所有在 [1, n] 范围之间没有出现在数组中的数字。 
# 
#  您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。 
# 
#  示例: 
# 
#  
# 输入:
# [4,3,2,7,8,2,3,1]
# 
# 输出:
# [5,6]
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        """
        哈希表
        时间复杂度O（n）
        空间复杂度O（n）
        """
        hashmap, res = {}, []
        for num in nums:
            hashmap[num] = 1
        for i in range(1, len(nums) + 1):
            if i not in hashmap:
                res.append(i)
        return res

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        """
        在原地计算，没有用到额外的空间
        """
        res = []
        # 例：nums[0]为4，nums[3]为2，则nums[4-1] = -2
        # 根据数组值（绝对值）找到对应索引（绝对值-1），将索引处值置为负
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        # 对于值不为负的索引，说明数组中没有该值（索引+1）
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res
        
# leetcode submit region end(Prohibit modification and deletion)

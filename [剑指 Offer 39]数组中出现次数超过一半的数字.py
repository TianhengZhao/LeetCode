# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。 
# 
#  
# 
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2 
# 
#  
# 
#  限制： 
# 
#  1 <= 数组长度 <= 50000 
# 
#  
# 
#  注意：本题与主站 169 题相同：https://leetcode-cn.com/problems/majority-element/ 
# 
#  
#  Related Topics 位运算 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        将nums中的 值:出现次数 存入哈希表
        """
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        for key in hashmap:
            if hashmap[key] > len(nums) // 2:
                return key
# leetcode submit region end(Prohibit modification and deletion)

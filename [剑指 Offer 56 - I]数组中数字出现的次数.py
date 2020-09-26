# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]
#  
# 
#  示例 2： 
# 
#  输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2] 
# 
#  
# 
#  限制： 
# 
#  
#  2 <= nums.length <= 10000

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def singleNumbers_ans(self, nums: List[int]) -> List[int]:
        xor_res = 0
        num1, num2 = 0, 0
        # 将nums中所有数进行异或，得到的就是num1和num2的异或结果
        for num in nums:
            xor_res ^= num
        sig = 1
        # sig为xor_res中第一个为1的位
        # 即num1和num2在该位中一个为1，一个为0
        while xor_res & sig == 0:
            sig <<= 1
        # 根据num的sig位是否为1，将其分为两组
        # 其中num1和num2一定在不同的组中
        # 相同的sum该位值相同，会被分到同一组中，异或之后为0，无影响
        for num in nums:
            if sig & num == 0:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]
# leetcode submit region end(Prohibit modification and deletion)

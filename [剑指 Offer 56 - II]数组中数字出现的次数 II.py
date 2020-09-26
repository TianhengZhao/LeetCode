# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [3,4,3,3]
# 输出：4
#  
# 
#  示例 2： 
# 
#  输入：nums = [9,1,7,9,7,9,7]
# 输出：1 
# 
#  
# 
#  限制： 
# 
#  
#  1 <= nums.length <= 10000 
#  1 <= nums[i] < 2^31


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            else:
                hashmap[num] += 1
        for key, val in hashmap.items():
            if not val:
                return key

    def singleNumber_ans(self, nums: List[int]) -> int:
        """
        对每个num的每一位求和模3，最终32位结果就是仅有的一个数
        """
        res = 0
        for i in range(32):
            count = 0
            # 当前计算的位
            bit = 1 << i
            for num in nums:
                if num & bit != 0:
                    # count为所有num当前位中1的个数
                    count += 1
            if count % 3 != 0:
                # res在该位上为1，由于bit除了最高位其他位为0，直接与res或，即可更新res
                res |= bit
        # 查看符号位
        return res - 2 ** 32 if res > 2 ** 31 - 1 else res

    def singleNumber_budong(self, nums: List[int]) -> int:
        """
        https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/solution/mian-shi-ti-56-ii-shu-zu-zhong-shu-zi-chu-xian-d-4/
        """
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones


# leetcode submit region end(Prohibit modification and deletion)

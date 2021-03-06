# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。 
# 
#  示例 1 : 
# 
#  
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
#  
# 
#  说明 : 
# 
#  
#  数组的长度为 [1, 20,000]。 
#  数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。 
#  
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """前缀和+哈希表"""
        res, pre = 0, 0
        # 存储前缀和出现的次数
        dic = collections.defaultdict(int)
        # 初始化
        dic[0] = 1
        for i in range(len(nums)):
            # 到nums[i]为止的前缀和
            pre += nums[i]
            # 如果有pre-k，说明有和为k的子串，次数为dic[pre - k]
            if pre - k in dic:
                res += dic[pre - k]
            dic[pre] += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)

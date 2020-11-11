# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。 
# 
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [3,2,3]
# 输出: 3 
# 
#  示例 2: 
# 
#  输入: [2,2,1,1,1,2,2]
# 输出: 2
#  
#  Related Topics 位运算 数组 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        哈希表 时间复杂度O(N) 空间复杂度O(N)
        """
        # 使用defaultdict为字典查询提供默认值
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        # 取得字典最大value值对应的key
        return max(hashmap.keys(), key=lambda x: hashmap[x])

    def majorityElementAns(self, nums: List[int]) -> int:
        """
        投票 时间复杂度O(N) 空间复杂度O(1)
        """
        candi, votes = None, 0
        for num in nums:
            # votes为0，重新选择candi
            if not votes:
                candi = num
                votes += 1
            # votes不为0， 和candi相同元素给其投1票，不相同投-1票
            elif num == candi:
                votes += 1
            else:
                votes -= 1
        # 多数元素将非多数元素都抵消掉了 最后剩下的一定是多数元素
        return candi
# leetcode submit region end(Prohibit modification and deletion)

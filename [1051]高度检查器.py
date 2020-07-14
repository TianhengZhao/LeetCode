# 学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。 
# 
#  请你返回能让所有学生以 非递减 高度排列的最小必要移动人数。 
# 
#  注意，当一组学生被选中时，他们之间可以以任何可能的方式重新排序，而未被选中的学生应该保持不动。 
#
#  
#  Related Topics 数组 



# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def heightChecker_mine(self, heights: List[int]) -> int:
        """
        先对序列排序
        再与原序列对比
        O（nlogn）
        """
        hei_in_order = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != hei_in_order[i]:
                count += 1
        return count

    def heightChecker(self, heights: List[int]) -> int:
        """
        先对序列桶排序
        再与原序列对比
        O（n）
        """
        buckets = [0] * 101
        for i in heights:
            buckets[i] += 1
        pos = 0
        count = 0
        for i in range(1, 101):
            while buckets[i] > 0:
                if i != heights[pos]:
                    count += 1
                pos += 1
                buckets[i] -= 1
        return count
# leetcode submit region end(Prohibit modification and deletion)

# 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对 (h, k) 表示，其中 h 是这个人的身高，k 是应该排在这个人前面且身高大于或等于 h 的人数
# 。 例如：[5,2] 表示前面应该有 2 个身高大于等于 5 的人，而 [5,0] 表示前面不应该存在身高大于等于 5 的人。 
# 
#  编写一个算法，根据每个人的身高 h 重建这个队列，使之满足每个整数对 (h, k) 中对人数 k 的要求。 
#
#  示例： 
#
# 输入：[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# 输出：[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#
#  提示： 
#
#  总人数少于 1100 人。 
#  
#  Related Topics 贪心算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def reconstructQueueAns(self, people: List[List[int]]) -> List[List[int]]:
        """时间复杂度O（n^2）"""
        res = []
        # 多级排序，按照身高降序排序，身高相同的按照人数升序排序
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        for person in people:
            if person[1] >= len(res):
                res.append(person)
            else:
                # 将小的直接插入到其该在的位置
                res.insert(person[1], person)
        return res

# leetcode submit region end(Prohibit modification and deletion)

# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
#  示例 1： 
# 
#  输入：head = [1,3,2]
# 输出：[2,3,1]
#  限制： 
# 
#  0 <= 链表长度 <= 10000 
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint_1(self, head: ListNode) -> List[int]:
        """每个链表值插入到列表头"""
        res = []
        while head:
            res.insert(0, head.val)
            head = head.next
        return res

    def reversePrint_2(self, head: ListNode) -> List[int]:
        """
        遍历后反转
        时间复杂度O（n）
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        # reverse()时间复杂度O（n）
        res.reverse()
        return res
# leetcode submit region end(Prohibit modification and deletion)

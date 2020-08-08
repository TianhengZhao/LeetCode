# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例: 
# 
#  给定 1->2->3->4, 你应该返回 2->1->4->3.
#  
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs_1(self, head: ListNode) -> ListNode:
        """迭代"""
        if not head or not head.next:
            return head

        sen = ListNode(-1)
        sen.next = head
        pre = sen

        lef, rig = head, head.next
        while rig:
            lef.next = rig.next
            rig.next = lef
            pre.next = rig
            pre = lef
            lef = lef.next
            rig = lef.next if lef else None
        return sen.next

    def swapPairs_2(self, head: ListNode) -> ListNode:
        """递归"""
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        # 交换
        first_node.next = self.swapPairs_2(second_node.next)
        second_node.next = first_node

        # 返回头结点
        return second_node

# leetcode submit region end(Prohibit modification and deletion)

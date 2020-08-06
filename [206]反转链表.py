# 反转一个单链表。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL 
# 
#  进阶: 
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？ 
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """可以转换为数组"""

    def reverseList_1(self, head: ListNode) -> ListNode:
        """
        迭代
        """
        pre = None
        cur = head
        while cur:
            # 先把原来cur.next位置存起来
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def reverseList_2(self, head: ListNode) -> ListNode:
        """递归"""
        if not head or not head.next:
            return head
        nextNode = self.reverseList_2(head.next)
        head.next.next = head
        head.next = None
        return nextNode



# leetcode submit region end(Prohibit modification and deletion)

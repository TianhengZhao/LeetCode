# 删除链表中等于给定值 val 的所有节点。 
# 
#  示例: 
# 
#  输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
#  
#  Related Topics 链表

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements_1(self, head: ListNode, val: int) -> ListNode:
        # 哨兵结点
        sentinel = ListNode(0)
        sentinel.next = head

        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        # 返回哨兵结点后一位
        return sentinel.next

    def removeElements_2(self, head: ListNode, val: int) -> ListNode:
        """
        未使用哨兵结点
        需要判断边界条件
        """
        # head为空
        if not head:
            return head
        # 开始几个结点值和val相等
        while head.val == val:
            head = head.next
            # 链表无结点
            if not head:
                return head
        # head是第一个结点值和val不同的结点
        pre = head
        now = head.next
        while now:
            if now.val == val:
                pre.next = now.next
            else:
                pre = pre.next
            now = now.next
        return head

# leetcode submit region end(Prohibit modification and deletion)

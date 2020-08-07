# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。 
# 
#  说明: 
# 1 ≤ m ≤ n ≤ 链表长度。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL 
#  Related Topics 链表 



# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head

        # 哨兵结点，避免讨论m=1的情况
        sen = ListNode(-1)
        sen.next = head

        pre = sen
        # pre指向m的前一位
        for _ in range(max(m-1, 0)):
            pre = pre.next
        # rar为反转后链表尾结点
        rar = p = pre.next
        # p指向反转链表的头，q是下一个头插入反转链表的结点
        q = p.next

        # tmp指向n后一位
        for _ in range(n-m):
            tmp = q.next
            q.next = p
            p = q
            q = tmp
        pre.next = p
        rar.next = q
        # 返回哨兵结点下一个结点
        return sen.next

# leetcode submit region end(Prohibit modification and deletion)

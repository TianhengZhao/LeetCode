# 给定单向链表的头指针和一个要删除的节点的指针，定义一个函数删除该节点。
# 
#  返回删除后的链表的头节点。 
#
# 
#  示例 1: 
# 
#  输入: head = 4 -> 5 -> 1 -> 9, val = 5 -> 1 -> 9
# 输出: 4 -> 1 -> 9
# 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
#
# 
#  说明：
#  题目保证链表中节点的值互不相同
#  
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: ListNode) -> ListNode:
        if not head or not val:
            return head
        # 待删除结点不是尾结点
        if not val.next:
            # val.next的信息赋给val，删除val.next
            tmp = val.next
            val.val = tmp.val
            val.next = tmp.next
        # 待删除结点为头结点
        elif head == val:
            head = None
        # 待删除结点为尾结点
        else:
            pre = head
            # 从头遍历至尾
            while pre.next.next:
                pre = pre.next
            pre.next = None
        return head



# leetcode submit region end(Prohibit modification and deletion)

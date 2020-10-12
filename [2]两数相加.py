# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。 
# 
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 
# 
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  示例： 
# 
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#  
#  Related Topics 链表 数学

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        # 哨兵结点
        sen = p = ListNode(-1)
        # 进位标志
        up = 0
        # 当p2不为空 或 p1不为空 或 进位不为0时，均继续计算
        while p1 or p2 or up:
            tmp = (p1.val if p1 else 0) + (p2.val if p2 else 0) + up
            # 无论是否有进位，均可模10
            node = ListNode(tmp % 10)
            # 用//10判断进位
            up = tmp // 10
            p.next = node
            p = p.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        return sen.next
# leetcode submit region end(Prohibit modification and deletion)

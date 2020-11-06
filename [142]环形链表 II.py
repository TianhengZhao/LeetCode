# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。 
# 
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，po
# s 仅仅是用于标识环的情况，并不会作为参数传递到函数中。 
# 
#  说明：不允许修改给定的链表。 
# 
#  进阶： 
# 
#  
#  你是否可以使用 O(1) 空间解决此题？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目范围在范围 [0, 104] 内 
#  -105 <= Node.val <= 105 
#  pos 的值为 -1 或者链表中的一个有效索引 
#  
#  Related Topics 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """建立哈希表，时间复杂度O(N) 空间复杂度O(N)"""

    def detectCycle(self, head: ListNode) -> ListNode:
        """
        快慢指针 时间复杂度O(N) 空间复杂度O(1)
        从同一起点head出发，先让快慢指针相遇
        pre再从head出发，和慢指针同时走，每次走一步
        pre和慢指针相遇的点就是环中第一个点
        """
        slow = fast = head
        while True:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            # 快慢指针相遇
            if slow == fast:
                pre = head
                # pre和slow同时走
                while pre != slow:
                    pre = pre.next
                    slow = slow.next
                return pre
# leetcode submit region end(Prohibit modification and deletion)

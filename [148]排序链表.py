# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 
# 
#  进阶： 
# 
#  
#  你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 5 * 104] 内 
#  -105 <= Node.val <= 105 
#  
#  Related Topics 排序 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        归并排序 时间复杂度O(NlogN) 空间复杂度O(1)
        分别两个间、四个间...比较，然后合并
        """
        if not head or not head.next:
            return head
        cur, length = head, 0
        while cur:
            cur = cur.next
            length += 1
        # 哨兵结点
        sen = ListNode(0)
        sen.next = head
        # 每次合并的规模
        intv = 1
        while intv < length:
            merge_point, cur = sen, sen.next
            # 定位此次要合并的结点h1
            while cur:
                h1, intv_count = cur, intv
                # 判断h1长度是否足够此次合并，是否存在h2
                while intv_count and cur:
                    cur = cur.next
                    intv_count -= 1
                # 链表结束，没有h2
                if intv_count:
                    break
                h2, intv_count = cur, intv
                while intv_count and cur:
                    cur = cur.next
                    intv_count -= 1
                # 计算h1长度，h2长度
                len1, len2 = intv, intv - intv_count
                # 合并
                while len1 and len2:
                    if h1.val < h2.val:
                        # merge_point是合并好的链表的最后一个结点
                        # merge_point.next是新合并进来的结点
                        merge_point.next = h1
                        h1 = h1.next
                        len1 -= 1
                    else:
                        merge_point.next = h2
                        h2 = h2.next
                        len2 -= 1
                    merge_point = merge_point.next
                # 如果一个已排好，另一个有剩余，剩下的都是大的，直接加在末尾
                if len1:
                    merge_point.next = h1
                else:
                    merge_point.next = h2
                # 为下一次合并做准备，将merge_point移到本次合并链表的末尾
                while len1 > 0 or len2 > 0:
                    merge_point = merge_point.next
                    len1 -= 1
                    len2 -= 1
                merge_point.next = cur
            # 合并规模增大一倍
            intv *= 2
        return sen.next
# leetcode submit region end(Prohibit modification and deletion)

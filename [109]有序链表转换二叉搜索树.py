# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。 
# 
# 一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
# 
#  示例: 
# 
#  给定的有序链表： [-10, -3, 0, 5, 9],
# 
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
# 
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#  
#  Related Topics 深度优先搜索 链表


# leetcode submit region begin(Prohibit modification and deletion)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    可以将链表转换为数组
    按照[108]生成
    """
    def sortedListToBST_1(self, head: ListNode) -> TreeNode:
        """
        按照中序遍历建造一个二叉树
        建立过程中
        二叉树生成节点值的顺序为链表次序（升序）
        该二叉树为二叉搜索树
        :param head:链表头指针
        :return:二叉搜索树根节点
        """
        p = head
        num = 0
        while p:
            num += 1
            p = p.next

        def helper(left, right):
            nonlocal head
            if left > right:
                return None
            mid = (left + right) // 2
            left = helper(left, mid - 1)
            node = TreeNode(head.val)
            node.left = left
            head = head.next
            node.right = helper(mid + 1, right)
            return node

        return helper(0, num - 1)

# leetcode submit region end(Prohibit modification and deletion)

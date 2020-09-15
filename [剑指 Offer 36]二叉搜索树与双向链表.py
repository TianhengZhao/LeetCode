# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。 
#
#  我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是
# 第一个节点。
#  特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。 
# 
#  
# 
#  注意：本题与主站 426 题相同：https://leetcode-cn.com/problems/convert-binary-search-tree-
# to-sorted-doubly-linked-list/ 
#  
#  Related Topics 分治算法

# leetcode submit region begin(Prohibit modification and deletion)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        先对二叉搜索树中根遍历
        得到的结果改为双向链表
        """
        # 二叉搜索树为空
        if not root:
            return None
        # 二叉搜索树只有一个结点
        if not root.left and not root.right:
            root.left, root.right = root, root
            return root
        # 中根遍历结果
        inorder = self.helper(root)
        # 改为双向链表
        for i in range(1, len(inorder) - 1):
            inorder[i].left = inorder[i - 1]
            inorder[i].right = inorder[i + 1]
        inorder[0].right, inorder[0].left = inorder[1], inorder[-1]
        inorder[-1].left, inorder[-1].right = inorder[-2], inorder[0]
        return inorder[0]

    def helper(self, node):
        """递归中根遍历"""
        if not node:
            return []
        return self.helper(node.left) + [node] + self.helper(node.right)

    def treeToDoublyList_ans(self, root: 'Node') -> 'Node':
        """
        直接在中根遍历时变换
        """
        def helper(node):
            if not node:
                return
            helper(node.left)
            # 非头结点，该结点和树中前驱结点链接
            if self.pre:
                self.pre.right = node
                node.left = self.pre
            # 头结点
            else:
                self.head = node
            self.pre = node
            helper(node.right)

        self.pre = None
        if not root:
            return None
        helper(root)
        # 头结点、尾结点相连
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

        
# leetcode submit region end(Prohibit modification and deletion)

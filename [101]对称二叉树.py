# 给定一个二叉树，检查它是否是镜像对称的。 
# 
#  
# 
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。 
# 
#      1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#  进阶： 
# 
#  你可以运用递归和迭代两种方法解决这个问题吗？ 
#  Related Topics 树 深度优先搜索 广度优先搜索 



# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSymmetric_1(self, root: TreeNode) -> bool:
        """
        递归
        """
        if not root:
            return True
        return self.is_sym(root.left, root.right)

    def is_sym(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2 or node1.val != node2.val:
            return False
        return self.is_sym(node1.left, node2.right) and self.is_sym(node1.right, node2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        """
        迭代，队列
        """
        if not root:
            return True
        deq = deque([(root.left, root.right)])
        while deq:
            node_l, node_r = deq.popleft()
            if not self.check(node_l, node_r):
                return False
            if node_l:
                deq.append((node_l.left, node_r.right))
                deq.append((node_l.right, node_r.left))
        return True

    def check(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2 or node1.val != node2.val:
            return False
        return True










# leetcode submit region end(Prohibit modification and deletion)

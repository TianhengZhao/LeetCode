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
    """
    和[100]类似
    """
    def isSymmetric_mine1(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            def check(node_l, node_r):
                if node_l is None and node_r is None:
                    return True
                if type(node_l) != type(node_r):
                    return False
                if node_l.val != node_r.val:
                    return False
                else:
                    return check(node_l.right, node_r.left) and check(node_l.left, node_r.right)

        return check(root.left, root.right)

    def isSymmetric_mine2(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def check(node_l, node_r):
            if not node_l and not node_r:
                return True
            if type(node_l) != type(node_r):
                return False
            if node_l.val != node_r.val:
                return False
            else:
                return True

        deq = deque([(root.left, root.right)])
        while deq:
            nodes = deq.popleft()
            if not check(nodes[0], nodes[1]):
                return False
            # 此时check（）结果为true，两个节点要么均为空，要么不为空值相同
            if nodes[0]:
                deq.append((nodes[0].left, nodes[1].right))
                deq.append((nodes[0].right, nodes[1].left))
        return True








# leetcode submit region end(Prohibit modification and deletion)

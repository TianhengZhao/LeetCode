# 给定两个二叉树，编写一个函数来检验它们是否相同。 
# 
#  如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。 
#
#
#  输入:      1          1
#           /           \
#          2             2
# 
#         [1,2],     [1,null,2]
# 
# 输出: false
#  
#
#  Related Topics 树 深度优先搜索

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree_other1(self, p: TreeNode, q: TreeNode) -> bool:
        """
        递归
        """
        # p，q均为空
        if not p and not q:
            return True
        # p，q一为空一不为空
        if not q or not p:
            return False
        # p，q值不相同
        if p.val != q.val:
            return False
        # p，q值相同
        return self.isSameTree_other1(p.right, q.right) and self.isSameTree_other1(p.left, q.left)

    def isSameTree_other2(self, p, q):
        """
        迭代
        """

        def check(p, q):
            if not p and not q:
                return True
            if not q or not p:
                return False
            # if p.val != q.val:
            if type(p) != type(q):
                return False
            return True

        deq = deque([(p, q), ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True
# leetcode submit region end(Prohibit modification and deletion)

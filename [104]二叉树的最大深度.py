# 给定一个二叉树，找出其最大深度。 
# 
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例： 
# 给定二叉树 [3,9,20,null,null,15,7]， 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回它的最大深度 3 。 
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
    def maxDepth_mine1(self, root: TreeNode) -> int:
        """
        自顶向下
        52ms
        """
        if not root:
            return 0
        dep = 0

        def depth(node, dep):
            dep += 1
            if not node.left and not node.right:
                return dep
            if node.left is None:
                return depth(node.right, dep)
            if node.right is None:
                return depth(node.left, dep)
            return max(depth(node.left, dep), depth(node.right, dep))

        return depth(root, dep)

    def maxDepth_other0(self, root: TreeNode) -> int:
        """
        ***
        自顶向下
        效率最高
        48ms
        """
        def top_down(node, h):
            # return h if node is None else max(top_down(node.left, h + 1), /
            # top_down(node.right, h + 1))
            if node is None:
                return h
            else:
                return max(top_down(node.left, h + 1), top_down(node.right, h + 1))

        return top_down(root, 0)

    def maxDepth_other1(self, root):
        """
        自底向上
        52ms
        """
        if root is None:
            return 0
        else:
            left_height = self.maxDepth_other1(root.left)
            right_height = self.maxDepth_other1(root.right)
            return max(left_height, right_height) + 1

    def maxDepth_mine2(self, root: TreeNode) -> int:
        """
        队列，广度优先
        68ms
        """
        if not root:
            return 0
        max_dep = 0
        deq = deque([(root, 1)])
        while deq:
            node = deq.popleft()
            if node[0].left is None and node[0].right is None:
                max_dep = max(max_dep, node[1])
                continue
            if node[0].left is None:
                deq.append((node[0].right, node[1] + 1))
                continue
            if node[0].right is None:
                deq.append((node[0].left, node[1] + 1))
                continue
            deq.append((node[0].right, node[1] + 1))
            deq.append((node[0].left, node[1] + 1))
        return max_dep

    def maxDepth_other3(self, root):
        """
        深度优先
        56ms
        """
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth
# leetcode submit region end(Prohibit modification and deletion)

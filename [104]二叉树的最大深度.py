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
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def maxDepth_1(self, root: TreeNode) -> int:
        """
        自顶向下
        """
        def top_down(node, h):
            if node is None:
                return h
            else:
                return max(top_down(node.left, h + 1), top_down(node.right, h + 1))

        return top_down(root, 0)

    def maxDepth_2(self, root):
        """
        自底向上
        """
        if not root:
            return 0
        return max(self.maxDepth_2(root.left), self.maxDepth_2(root.right)) + 1
# leetcode submit region end(Prohibit modification and deletion)

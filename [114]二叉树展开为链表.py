# 给定一个二叉树，原地将它展开为一个单链表。 
# 
#  
# 
#  例如，给定二叉树 
# 
#      1
#    / \
#   2   5
#  / \   \
# 3   4   6 
# 
#  将其展开为： 
# 
#  1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6 
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        得到先根遍历结果
        形成链表，去掉每个节点左孩子
        """
        if not root:
            return root
        pre_ls = self.preorder(root)
        for i in range(len(pre_ls) - 1):
            pre_ls[i].right = pre_ls[i + 1]
            pre_ls[i].left = None

    def preorder(self, root):
        if not root:
            return []
        return [root] + self.preorder(root.left) + self.preorder(root.right)

    def flatten_2(self, root: TreeNode) -> None:
        """
        迭代实现先根遍历
        每遍历到一个节点 接入链表中
        """
        if not root:
            return

        stack = [root]
        prev = None

        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = curr

    def flatten_3(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right

        
# leetcode submit region end(Prohibit modification and deletion)

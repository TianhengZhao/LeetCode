# 给定一个二叉树，返回它的中序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# 输出: [1,3,2] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal_mine(self, root: TreeNode) -> List[int]:
        """
        递归
        """
        res = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res

    def inorderTraversal_other(self, root: TreeNode) -> List[int]:
        """
        迭代，效率较高
        """
        res = []
        stack = []
        p = root
        # 同时判断p和stack是否为空
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            # 若p为空 直接执行此处
            p = stack.pop()
            res.append(p.val)
            p = p.right
        return res

    def inorderTraversal_other1(self, root: TreeNode) -> List[int]:
        """
        迭代，效率较低
        """
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

# leetcode submit region end(Prohibit modification and deletion)

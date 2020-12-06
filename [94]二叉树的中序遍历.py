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
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        """
        递归
        """
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, node, res):
        if not node:
            return
        self.inorder(node.left, res)
        res.append(node.val)
        self.inorder(node.right, res)

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        迭代，效率较高
        """
        res, stack, p = [], [], root
        # 同时判断p和stack是否为空
        while p or stack:
            # 最左
            while p:
                stack.append(p)
                p = p.left
            # 若p为空 直接执行此处
            node = stack.pop()
            res.append(node.val)
            p = node.right
        return res

# leetcode submit region end(Prohibit modification and deletion)

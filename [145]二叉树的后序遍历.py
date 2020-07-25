# 给定一个二叉树，返回它的 后序 遍历。 
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
# 输出: [3,2,1] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, node, res):
        if not node:
            return
        self.helper(node.left, res)
        self.helper(node.right, res)
        res.append(node.val)

    def postorderTraversal_m(self, root: TreeNode) -> List[int]:
        """
        递归
        """
        res = []
        self.helper(root, res)
        return res

    def postorderTraversal_1(self, root: TreeNode) -> List[int]:
        """
        迭代
        自顶向下，按照root，right，left顺序出栈
        对结果倒序即为后根遍历的结果，自底向上，left，right，root
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        return output[::-1]

    def postorderTraversal_2(self, root: TreeNode) -> List[int]:
        """
        *正常思路后根遍历
        """
        res = []
        stack = []
        node = root
        while stack or node:
            # 获得最左叶子结点
            while node:
                stack.append(node)
                node = node.left if node.left else node.right
            node = stack.pop()
            res.append(node.val)
            if stack and stack[-1].left == node:
                # 从node父节点的右子节点开始遍历
                node = stack[-1].right
            else:
                # 若栈不为空，继续弹栈
                node = None
        return res

# leetcode submit region end(Prohibit modification and deletion)

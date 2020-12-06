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

    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        """
        递归
        """
        res = []
        self.helper(root, res)
        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        迭代
        自顶向下，按照root，right，left顺序出栈
        对结果倒序即为后根遍历的结果，自底向上，left，right，root
        """
        if not root:
            return []
        stack, res = [root], []
        while stack:
            # 弹出node，将node的左右子节点入栈
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]

    def postorderTraversal3(self, root: TreeNode) -> List[int]:
        """
        迭代
        """
        res, stack, p = [], [], root
        while stack or p:
            # 获得最左叶子结点
            while p:
                stack.append(p)
                # 如果p没有左子节点了，p指向其右子节点，继续找最左结点
                p = p.left if p.left else p.right
            node = stack.pop()
            res.append(node.val)
            # 如果node为其父节点的左子节点
            if stack and stack[-1].left == node:
                # 从node父节点的右子节点开始遍历
                p = stack[-1].right
            else:
                # 若栈不为空，继续弹栈
                p = None
        return res

# leetcode submit region end(Prohibit modification and deletion)

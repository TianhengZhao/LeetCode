# 给定一个二叉树，返回它的 前序 遍历。 
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
# 输出: [1,2,3]
#  
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
        res.append(node.val)
        self.helper(node.left,res)
        self.helper(node.right,res)

    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        """
        递归
        """
        res = []
        self.helper(root, res)
        return res

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        迭代
        """
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
# leetcode submit region end(Prohibit modification and deletion)

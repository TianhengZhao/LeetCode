# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例： 
# 二叉树：[3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层次遍历结果： 
# 
#  [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder_1(self, root: TreeNode) -> List[List[int]]:
        """
        宽度优先，迭代
        """
        if not root:
            return []
        layer = deque()
        layer.append(root)
        res = []
        while layer:
            cur_layer = []
            # 当前队列内所有结点即为该层次所有结点
            for _ in range(len(layer)):
                node = layer.popleft()
                cur_layer.append(node.val)
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
            res.append(cur_layer)
        return res

    def levelOrder_2(self, root):
        """
        递归
        """
        res = []
        self.level(root, 0, res)
        return res

    def level(self, root, level, res):
        if not root:
            return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        if root.left:
            self.level(root.left, level + 1, res)
        if root.right:
            self.level(root.right, level + 1, res)
# leetcode submit region end(Prohibit modification and deletion)

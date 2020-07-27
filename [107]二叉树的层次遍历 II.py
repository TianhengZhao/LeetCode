# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历） 
# 
#  例如： 
# 给定二叉树 [3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其自底向上的层次遍历为： 
# 
#  [
#   [15,7],
#   [9,20],
#   [3]
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
    def levelOrderBottom_m0(self, root):
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
            # 插入到头部即可
            res.insert(0, cur_layer)
        return res

    def levelOrderBottom_m1(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.lob(root, 0, res)
        return res[::-1]

    def lob(self, node, level, res):
        if not node:
            return
        if len(res) == level:
            res.append([])
        res[level].append(node.val)
        if node.left:
            self.lob(node.left, level+1, res)
        if node.right:
            self.lob(node.right, level+1, res)

    def levelOrderBottom_m2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        layer = deque()
        layer.append((root, 0))
        res = []
        while layer:
            node, cur = layer.popleft()
            if len(res) == cur:
                res.append([])
            res[cur].append(node.val)
            if node.left:
                layer.append((node.left, cur + 1))
            if node.right:
                layer.append((node.right, cur + 1))
        return res[::-1]
# leetcode submit region end(Prohibit modification and deletion)

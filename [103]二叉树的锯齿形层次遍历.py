# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。 
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
#  返回锯齿形层次遍历如下： 
# 
#  [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
#  Related Topics 栈 树 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        用flag判断是否翻转
        层次遍历方法同[102]
        """
        if not root:
            return []
        que = deque([root])
        res = []
        fla = True
        while que:
            length = len(que)
            layer = []
            for _ in range(length):
                node = que.popleft()
                if fla:
                    layer.append(node.val)
                else:
                    # layer.insert(0, node.val)    O(n)
                    layer = [node.val] + layer
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            fla = not fla
            res.append(layer)
        return res

# leetcode submit region end(Prohibit modification and deletion)

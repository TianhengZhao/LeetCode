# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。 
# 
#  
# 
#  例如: 
# 给定二叉树: [3,9,20,null,null,15,7], 
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
#   [20,9],
#   [15,7]
# ]
#
#  提示： 
# 
#  
#  节点总数 <= 1000 
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, flag = [], True
        que = deque([root])
        while que:
            tmp = []
            for _ in range(len(que)):
                node = que.popleft()
                # flag为True，顺序
                if flag:
                    tmp.append(node.val)
                # 否则，倒序
                else:
                    tmp = [node.val] + tmp
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            flag = not flag
            res.append(tmp)
        return res
# leetcode submit region end(Prohibit modification and deletion)

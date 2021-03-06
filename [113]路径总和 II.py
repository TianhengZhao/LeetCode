# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 给定如下二叉树，以及目标和 sum = 22， 
# 
#                5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#  
# 
#  返回: 
# 
#  [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#  
#  Related Topics 树 深度优先搜索 

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, summ: int) -> List[List[int]]:
        """回溯"""
        res = []
        self.backtrack(root, summ, [], res)
        return res

    def backtrack(self, root, total, path, res):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right and total == root.val:
            res.append(path[:])
        else:
            self.backtrack(root.left, total - root.val, path, res)
            self.backtrack(root.right, total - root.val, path, res)
        # 清除自己出现过的痕迹
        path.pop()






# leetcode submit region end(Prohibit modification and deletion)

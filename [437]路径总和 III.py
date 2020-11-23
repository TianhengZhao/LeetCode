# 给定一个二叉树，它的每个结点都存放着一个整数值。 
# 
#  找出路径和等于给定数值的路径总数。 
# 
#  路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。 
# 
#  二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。 
# 
#  示例： 
# 
#  root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
# 
# 返回 3。和等于 8 的路径有:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
#  
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.dfs(root, sum, [])

    def dfs(self, root, sum, sum_rec):
        """
        用sum_rec记录所有出现过的和
        计算sum_rec中sum数量即可
        """
        if not root:
            return 0
        sum_rec = [root.val + i for i in sum_rec] + [root.val]
        res = sum_rec.count(sum)
        return res + self.dfs(root.left, sum, sum_rec) + self.dfs(root.right, sum, sum_rec)

        
# leetcode submit region end(Prohibit modification and deletion)

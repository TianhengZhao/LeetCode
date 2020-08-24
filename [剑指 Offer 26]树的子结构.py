# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构) 
# 
#  B是A的子结构， 即 A中有出现和B相同的结构和节点值。 
# 
#  例如: 
# 给定的树 A: 
# 
#  3 
#  / \ 
#  4 5 
#  / \ 
#  1 2 
# 给定的树 B： 
# 
#  4 
#  / 
#  1 
# 返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。 
# 
#  示例 1： 
# 
#  输入：A = [1,2,3], B = [3,1]
# 输出：false
#  
# 
#  示例 2： 
# 
#  输入：A = [3,4,5,1,2], B = [4,1]
# 输出：true 
# 
#  限制： 
# 
#  0 <= 节点个数 <= 10000 
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        """
        对A先根遍历，找到与B值相同的节点
        该节点与B比较，看结构是否相同
        """
        if not B:
            return False
        seq = self.dfs(A)
        for node in seq:
            if node.val == B.val and self.is_same(node, B):
                return True
        return False

    def dfs(self, root):
        """先根遍历"""
        if not root:
            return []
        return [root] + self.dfs(root.left) + self.dfs(root.right)

    def is_same(self, node1, node2):
        """
        node1和node2逐个结点比较
        结构相同包括node1包含node2，但是node1还会有子孙结点
        """
        # node2遍历结束即可，允许node1有子孙结点
        if not node2:
            return True
        # node2未空，node1空 或者二者值不同
        if not node1 or node1.val != node2.val:
            return False
        return self.is_same(node1.left, node2.left) and self.is_same(node1.right, node2.right)

    def isSubStructure_ans(self, A: TreeNode, B: TreeNode) -> bool:
        """直接遍历"""
        if not A or not B:
            return False
        return self.is_same(A, B) or self.isSubStructure_ans(A.left, B) or self.isSubStructure_ans(A.right, B)

# leetcode submit region end(Prohibit modification and deletion)

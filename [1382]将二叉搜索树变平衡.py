# 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。 
# 
# 如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是平衡的 。
# 
# 如果有多种构造方法，请你返回任意一种。
#  示例：
#  输入：root = [1,null,2,null,3,null,4,null,null]
# 输出：[2,1,3,null,null,null,4]
# 解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
#  提示：
#  树节点的数目在 1 到 10^4 之间。 
#  树节点的值互不相同，且在 1 到 10^5 之间。 
#  
#  Related Topics 二叉搜索树 



# leetcode submit region begin(Prohibit modification and deletion)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        先得到该树的中根遍历结果
        再构造平衡树[108]
        """
        ino = []
        self.inorder(root, ino)
        return self.create_bst(0, len(ino)-1, ino)

    def inorder(self, node, res):
        if not node:
            return
        self.inorder(node.left, res)
        res.append(node.val)
        self.inorder(node.right, res)

    def create_bst(self, left, right, ino):
        if left > right:
            return None
        mid = (right - left) // 2 + left
        node = TreeNode(ino[mid])
        node.left = self.create_bst(left, mid - 1, ino)
        node.right = self.create_bst(mid + 1, right, ino)
        return node

# leetcode submit region end(Prohibit modification and deletion)

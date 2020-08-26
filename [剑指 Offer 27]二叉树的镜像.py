# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。 
# 
#  例如输入： 
# 
#  4 
#  / \ 
#  2 7 
#  / \ / \ 
# 1 3 6 9 
# 镜像输出： 
# 
#  4 
#  / \ 
#  7 2 
#  / \ / \ 
# 9 6 3 1 
# 
#  
# 
#  示例 1： 
# 
#  输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
#  
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 1000 
# 
#  注意：本题与主站 226 题相同：https://leetcode-cn.com/problems/invert-binary-tree/ 
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree_1(self, root: TreeNode) -> TreeNode:
        """生成新树，返回新建的结点"""
        if not root:
            return None
        node = TreeNode(root.val)
        node.right = self.mirrorTree_1(root.left)
        node.left = self.mirrorTree_1(root.right)
        return node

    def mirrorTree_ans(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        # tmp = root.left   暂存左子节点，因为下一行代码会改变左子节点
        # root.left = self.mirrorTree(root.right)
        # root.right = self.mirrorTree(tmp)

        # 平行赋值时，先将右侧打包成元组，再赋给左侧。省去了暂存操作
        root.left, root.right = self.mirrorTree_ans(root.right), self.mirrorTree_ans(root.left)
        return root

# leetcode submit region end(Prohibit modification and deletion)

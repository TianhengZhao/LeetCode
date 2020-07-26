# 根据一棵树的中序遍历与后序遍历构造二叉树。 
# 
#  注意: 
# 你可以假设树中没有重复的元素。 
# 
#  例如，给出 
# 
#  中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3] 
# 
#  返回如下的二叉树： 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
#  Related Topics 树 深度优先搜索 数组 


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        index = {element: i for i, element in enumerate(inorder)}

        def helper(post_left, post_right, in_left, in_right):
            if post_left > post_right:
                return None
            node = TreeNode(postorder[post_right])
            in_root = index[postorder[post_right]]
            post_right_num = in_right - in_root
            node.left = helper(post_left, post_right - post_right_num - 1, in_left, in_root - 1)
            node.right = helper(post_right - post_right_num, post_right - 1, in_root + 1, in_right)
            return node

        length = len(inorder)
        return helper(0, length - 1, 0, length - 1)
# leetcode submit region end(Prohibit modification and deletion)

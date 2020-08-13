# 根据一棵树的前序遍历与中序遍历构造二叉树。 
# 
#  注意: 
# 你可以假设树中没有重复的元素。 
# 
#  例如，给出 
# 
#  前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7] 
# 
#  返回如下的二叉树： 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
#  Related Topics 树 深度优先搜索 数组 



# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index = {element: x for x, element in enumerate(inorder)}

        def helper(pre_start, pre_end, in_left, in_right):
            if pre_start > pre_end:
                return None
            root = TreeNode(preorder[pre_start])
            in_root = index[preorder[pre_start]]
            root.left = helper(pre_start+1, pre_start+in_root-in_left, in_left, in_root-1)
            root.right = helper(pre_start+in_root-in_left+1, pre_end, in_root+1, in_right)
            return root

        return helper(0, len(preorder)-1, 0, len(inorder)-1)
# leetcode submit region end(Prohibit modification and deletion)

# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。 
# 
#  本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。 
# 
#  示例: 
# 
#  给定有序数组: [-10,-3,0,5,9],
# 
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
# 
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
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

    def sortedArrayToBST_1(self, nums: List[int]) -> TreeNode:
        return self.helper(0, len(nums) - 1, nums)

    def helper(self, left, right, nums):
        """
        :param left: 本次递归 列表的左边界
        :param right: 列表的右边界
        :param nums: 列表
        :return: 本次确定的结点，即列表的中间结点
        """
        if left > right:
            return None

        mid = (left + right) // 2

        root = TreeNode(nums[mid])
        root.left = self.helper(left, mid - 1, nums)
        root.right = self.helper(mid + 1, right, nums)
        return root



# leetcode submit region end(Prohibit modification and deletion)

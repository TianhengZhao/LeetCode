# 二叉搜索树中的两个节点被错误地交换。 
# 
#  请在不改变其结构的情况下，恢复这棵树。 
# 
#  示例 1: 
# 
#  输入: [1,3,null,null,2]
# 
#    1
#   /
#  3
#   \
#    2
# 
# 输出: [3,1,null,null,2]
# 
#    3
#   /
#  1
#   \
#    2
#  
# 
#  示例 2: 
# 
#  输入: [3,1,4,null,null,2]
# 
#   3
#  / \
# 1   4
#    /
#   2
# 
# 输出: [2,1,4,null,null,3]
# 
#   2
#  / \
# 1   4
#    /
#   3 
# 
#  进阶: 
# 
#  
#  使用 O(n) 空间复杂度的解法很容易实现。 
#  你能想出一个只使用常数空间的解决方案吗？ 
#  
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        nums = self.inorder(root)
        num1, num2 = self.find_two_swapped(nums)
        self.recover(root, 2, num1, num2)

    def inorder(self, root):
        """递归中根遍历"""
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

    def find_two_swapped(self, nums):
        """
        *
        由中序遍历结果得到交换的两个值
        大的一定在小的左侧
        出现两个逆序
        第一个逆序较大的数
        第二个逆序较小的数
        """
        n = len(nums)
        x = y = -1
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                y = nums[i + 1]
                if x == -1:
                    # 第一个逆序
                    x = nums[i]
                else:
                    # 第二个逆序，此时y = nums[i + 1]
                    break
        return x, y

    def recover(self, root, count, num1, num2):
        """恢复二叉搜索树中交换的值"""
        if root:
            if root.val == num1 or root.val == num2:
                root.val = num2 if root.val == num1 else num1
                # 交换次数-1
                count -= 1
                if count == 0:
                    return
            self.recover(root.left, count, num1, num2)
            self.recover(root.right, count, num1, num2)
        
# leetcode submit region end(Prohibit modification and deletion)

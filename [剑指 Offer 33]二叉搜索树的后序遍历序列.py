# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。 
# 
#  
# 
#  参考以下这颗二叉搜索树： 
# 
#       5
#     / \
#    2   6
#   / \
#  1   3 
# 
#  示例 1： 
# 
#  输入: [1,6,3,2,5]
# 输出: false 
# 
#  示例 2： 
# 
#  输入: [1,3,2,6,5]
# 输出: true 
# 
#  
# 
#  提示： 
# 
#  
#  数组长度 <= 1000 
#


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        """
        递归方法
        二叉搜索树后根遍历，列表中第一个比根大的数为右子树第一个结点，即根左右子树分界
        判断右子树中所有元素都比根结点大
        再分别对左右子树递归判断
        """
        if len(postorder) == 1 or len(postorder) == 0:
            return True
        for i in range(len(postorder)):
            if postorder[i] > postorder[-1]:
                break
        # right为分界点或者根本身（无右子树）
        right = i
        # 判断右子树所有元素是否大于根
        for i in range(right, len(postorder)-1):
            if postorder[i] < postorder[-1]:
                return False
        return self.verifyPostorder(postorder[:right]) and self.verifyPostorder(postorder[right: len(postorder)-1])

# leetcode submit region end(Prohibit modification and deletion)

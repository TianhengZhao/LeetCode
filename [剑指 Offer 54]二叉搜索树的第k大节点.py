# 给定一棵二叉搜索树，请找出其中第k大的节点。 
# 
#  
# 
#  示例 1: 
# 
#  输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4 
# 
#  示例 2: 
# 
#  输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 4 
# 
#  
# 
#  限制： 
# 
#  1 ≤ k ≤ 二叉搜索树元素个数 
#  Related Topics 树 
#  👍 68 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """中根遍历取倒数第k个"""
        order = self.inorder(root)
        return order[-k]

    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)

    def kthLargest_ans(self, root: TreeNode, k: int) -> int:
        """逆向中根遍历"""
        stack, node = [], root
        while node or stack:
            if node:
                stack.append(node)
                node = node.right
            else:
                cur = stack.pop()
                k -= 1
                if not k:
                    return cur.val
                if cur.left:
                    node = cur.left

# leetcode submit region end(Prohibit modification and deletion)

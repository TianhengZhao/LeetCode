# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。 
# 
#  进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？ 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#  
# 
#  示例 2： 
# 
#  输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#
#  提示： 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -106 <= nums1[i], nums2[i] <= 106 
#  
#  Related Topics 数组 二分查找 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMedianSortedArraysCopy(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        # 长度为奇数
        if length % 2 == 1:
            return self.getKthElement(nums1, nums2, (length + 1) // 2)
        # 长度为偶数，中间两个数的平均数
        else:
            return (self.getKthElement(nums1, nums2, length // 2) + self.getKthElement(nums1, nums2, length // 2 + 1)) / 2

    def getKthElement(self, nums1, nums2, k):
        """
        假如nums1和nums2升序合并后，找第k个位置的值
        二分查找
        """
        len1, len2 = len(nums1), len(nums2)
        # 查询起始索引
        index1, index2 = 0, 0
        while True:
            # nums1查完了，在nums2中index2开始的第k个
            if index1 == len1:
                return nums2[index2 + k - 1]
            if index2 == len2:
                return nums1[index1 + k - 1]
            # 在nums1或nums2的当前位置找到
            if k == 1:
                return min(nums1[index1], nums2[index2])
            # 要找第k个位置，分别在nums1、nums2的index后的k // 2位置作比较
            new_index1 = min(index1 + k // 2 - 1, len1 - 1)
            new_index2 = min(index2 + k // 2 - 1, len2 - 1)
            pivot1, pivot2 = nums1[new_index1], nums2[new_index2]
            # 在index1到new_index1中间的数是不符合要求的，将其剔除，重置index，再进行查找
            if pivot1 <= pivot2:
                k -= new_index1 - index1 + 1
                index1 = new_index1 + 1
            else:
                k -= new_index2 - index2 + 1
                index2 = new_index2 + 1
# leetcode submit region end(Prohibit modification and deletion)

# 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组： 
# 
#  
#  若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]； 
#  或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。 
#  
# 
#  也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。 
# 
#  返回 A 的最大湍流子数组的长度。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[9,4,2,10,7,8,8,1,9]
# 输出：5
# 解释：(A[1] > A[2] < A[3] > A[4] < A[5])
#  
# 
#  示例 2： 
# 
#  输入：[4,8,12,16]
# 输出：2
#  
# 
#  示例 3： 
# 
#  输入：[100]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 40000 
#  0 <= A[i] <= 10^9 
#  
#  Related Topics 数组 动态规划 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxTurbulenceSize_ans(self, A: List[int]) -> int:
        """
        动态规划
        """
        # 长度为1或者A中值均相等
        if len(A) == 1 or min(A) == max(A):
            return 1
        # cur存放当前长度，res为最大长度
        cur, res = 1, 1
        for k in range(1, len(A) - 1):
            if A[k - 1] < A[k] > A[k + 1] or A[k - 1] > A[k] < A[k + 1]:
                cur += 1
                if cur > res:
                    res = cur
            else:
                cur = 1
        return res + 1
        
# leetcode submit region end(Prohibit modification and deletion)

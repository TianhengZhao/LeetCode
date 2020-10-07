# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i
# +1]×…×A[n-1]。不能使用除法。
#  示例: 
# 
#  输入: [1,2,3,4,5]
# 输出: [120,60,40,30,24]
#  
#  所有元素乘积之和不会溢出 32 位整数 
#  a.length <= 100000


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def constructArr_ans(self, a: List[int]) -> List[int]:
        """
        https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/solution/mian-shi-ti-66-gou-jian-cheng-ji-shu-zu-biao-ge-fe/
        上下两个三角的方法
        """
        b = [1] * len(a)
        # 下三角
        for i in range(1, len(a)):
            b[i] = a[i - 1] * b[i - 1]
        tmp = 1
        # 从下往上乘，上三角
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]
            b[i] *= tmp
        return b
# leetcode submit region end(Prohibit modification and deletion)

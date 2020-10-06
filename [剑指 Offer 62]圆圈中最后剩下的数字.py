# 0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。 
# 
#  例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。 
# 
#  
# 
#  示例 1： 
# 
#  输入: n = 5, m = 3
# 输出: 3
#  
# 
#  示例 2： 
# 
#  输入: n = 10, m = 17
# 输出: 2
#  
# 
#  
# 
#  限制： 
# 
#  
#  1 <= n <= 10^5 
#  1 <= m <= 10^6


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        """放入数组 时间复杂度较高"""
        nums = [i for i in range(n)]
        pos = -1
        for i in range(n - 1):
            tmp = (pos + m) % len(nums)
            del nums[tmp]
            pos = tmp - 1
        return nums[0]

    def lastRemaining_ans(self, n: int, m: int) -> int:
        """
        数学法 逆向推理
        https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/javajie-jue-yue-se-fu-huan-wen-ti-gao-su-ni-wei-sh/
        """
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f
# leetcode submit region end(Prohibit modification and deletion)

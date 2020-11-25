# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。 
# 
#  给出两个整数 x 和 y，计算它们之间的汉明距离。 
# 
#  注意： 
# 0 ≤ x, y < 231. 
# 
#  示例: 
# 
#  
# 输入: x = 1, y = 4
# 
# 输出: 2
# 
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# 
# 上面的箭头指出了对应二进制位不同的位置。
#  
#  Related Topics 位运算


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hammingDistance1(self, x: int, y: int) -> int:
        """
        计算x，y异或结果中1的位数
        一位一位地算1的个数
        """
        cal = x ^ y
        res = 0
        while cal:
            if cal & 1:
                res += 1
            cal >>= 1
        return res

    def hammingDistance2(self, x, y):
        """
         cal & (cal - 1)，每次将cal最右的1变为0， 有几个1循环几次，不用有几位循环几次
        """
        cal = x ^ y
        res = 0
        while cal:
            res += 1
            cal = cal & (cal - 1)
        return res


        
# leetcode submit region end(Prohibit modification and deletion)

# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, 
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。 
# 
#  说明：你不能倾斜容器，且 n 的值至少为 2。 
# 
#  
# 
#  
# 
#  图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。 
# 
#  
# 
#  示例： 
# 
#  输入：[1,8,6,2,5,4,8,3,7]
# 输出：49 
#  Related Topics 数组 双指针 



# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxArea_other(self, height: List[int]) -> int:
        """
        双指针i,j，分别从头、尾向内移动
         h[i]、h[j]中较短的向内移动一格
         宽度减小，移动短柱，面积可能大可能小可能不变
         （该短柱相当于已遍历中间所有柱子，和该长柱面积是最大的）
         移动长柱，面积一定变小
         每次移动的结果和res取最大
        """
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

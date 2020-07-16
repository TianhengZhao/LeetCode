# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和
# 。假定每组输入只存在唯一答案。 
#
#  示例： 
# 
#  输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 10^3 
#  -10^3 <= nums[i] <= 10^3 
#  -10^4 <= target <= 10^4 
#  
#  Related Topics 数组 双指针 



# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def threeSumClosest_mine(self, nums: List[int], target: int) -> int:
        """
        与[15]三数之和类似
        先排序
        若i，left，right位置元素和小于target，left右移一位
        反之亦然
        """
        dis = 1.3e4
        nums.sort()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                res = nums[i] + nums[left] + nums[right]
                if res < target:
                    if (target - res) < dis:
                        dis = target - res
                        ans = res
                    left += 1
                elif res > target:
                    if (res - target) < dis:
                        dis = res - target
                        ans = res
                    right -= 1
                else:
                    return target
        return ans
# leetcode submit region end(Prohibit modification and deletion)

# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c +
#  d 的值与 target 相等？找出所有满足条件且不重复的四元组。 

#  答案中不可以包含重复的四元组。 
# 
#  示例： 
# 
#  给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#  
#  Related Topics 数组 哈希表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def fourSum_mine(self, nums: List[int], target: int) -> List[List[int]]:
        """
        与三数之和思路类似，外加一层for循环
        """
        length = len(nums)
        if length < 4:
            return []
        res = []
        nums.sort()
        for fir in range(length - 3):
            if fir >= 1 and nums[fir] == nums[fir - 1]:
                continue
            for sec in range(fir + 1, length - 2):
                if sec >= fir + 2 and nums[sec] == nums[sec - 1]:
                    continue
                left = sec + 1
                right = length - 1
                while left < right:
                    temp = nums[fir] + nums[sec] + nums[left] + nums[right]
                    if temp < target:
                        left += 1
                    elif temp > target:
                        right -= 1
                    else:
                        res.append([nums[fir], nums[sec], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while right > left and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res

    def fourSum_other(self, nums: List[int], target: int) -> List[List[int]]:
        """
        主要思路同上
        增加了条件剪枝，减少不必要的循环
        """
        n = len(nums)
        if not nums or n < 4:
            return []
        nums.sort()  # 升序
        res = []
        for i in range(n - 3):
            # i处连续四个数之和大于target，在i之后不可能有符合的结果
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # i处元素和序列最大的3数之和仍小于target，i处不会有符合的结果，i右移
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                # j和i做类似判断，先比最小值，大于target，结束
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                # 再比最大值，大于target，j右移
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                if j - i > 1 and nums[j] == nums[j - 1]:
                    continue
                L = j + 1
                R = n - 1
                while L < R:
                    if nums[i] + nums[j] + nums[L] + nums[R] == target:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        while L < R and nums[L] == nums[L + 1]:
                            L = L + 1
                        while L < R and nums[R] == nums[R - 1]:
                            R = R - 1
                        L = L + 1
                        R = R - 1
                    elif nums[i] + nums[j] + nums[L] + nums[R] > target:
                        R = R - 1
                    else:
                        L = L + 1
        return res

    def fourSum_other1(self, nums: List[int], target: int) -> List[List[int]]:
        """
        利用哈希表，与两数之和类似
        四个数分为两组
        可哈希的数据类型，即不可变的数据结构(字符串str、元组tuple、对象集objects)
        不可哈希的数据类型，即可变的数据结构 (字典dict，列表list，集合set)
        """
        length = len(nums)
        if length < 4:
            return []
        # 集合，去重
        res = set()
        nums.sort()
        hashmap = {}
        for i in range(length - 1):
            for j in range(i + 1, length):
                res1 = nums[i] + nums[j]
                # 之前出现过res2 = target - res1，且已经存在哈希表中
                if target - res1 in hashmap:
                    # tmp 为res2的每对索引
                    for tmp in hashmap[target - res1]:
                        # 为了避免结果重复，tmp[0], tmp[1], i, j递增才存入结果
                        if tmp[1] < i:
                            # 元组可哈希
                            res.add((nums[tmp[0]], nums[tmp[1]], nums[i], nums[j]))
                # 哈希表的value为列表，存储一对对索引值
                if res1 not in hashmap:
                    hashmap[res1] = []
                # 索引值对是元组形式，可哈希
                hashmap[res1].append((i, j))
        # 将元组转换为列表
        ans = []
        for r in res:
            ans.append(list(r))
        return ans



# leetcode submit region end(Prohibit modification and deletion)

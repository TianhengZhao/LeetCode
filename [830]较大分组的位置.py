# 在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。 
# 
#  例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。 
# 
#  分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示
# 为 [3,6] 。 
# 
#  我们称所有包含大于或等于三个连续字符的分组为 较大分组 。 
# 
#  找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abbxxxxzzy"
# 输出：[[3,6]]
# 解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "aaa"
# 输出：[[0,2]]
#
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅含小写英文字母 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start, end = 0, 0
        res = []
        # 避免末尾出现三连判断不出来，示例2情况
        s = s + '1'
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                end += 1
            else:
                if (end - start) >= 2:
                    res.append([start, end])
                start = i
                end = start
        return res
# leetcode submit region end(Prohibit modification and deletion)

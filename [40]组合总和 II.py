# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用一次。 
# 
#  说明： 
# 
#  
#  所有数字（包括目标数）都是正整数。 
#  解集不能包含重复的组合。 
#  
# 
#  示例 1: 
# 
#  输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#  
# 
#  示例 2: 
# 
#  输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ] 
#  Related Topics 数组 回溯算法 
#  👍 424 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        candidates.sort()
        self.res = []
        self.backtrack(candidates, target, [], 0)
        return self.res

    def backtrack(self, candidates, target, path, cal):
        if target == 0:
            self.res.append(path.copy())
            return
        for i in range(cal, len(candidates)):
            if target - candidates[i] < 0:
                break
            # 横向剪去重复值，纵向不剪
            if i > cal and candidates[i] == candidates[i - 1]:
                continue
            self.backtrack(candidates, target - candidates[i], path + [candidates[i]], i + 1)
# leetcode submit region end(Prohibit modification and deletion)

# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的数字可以无限制重复被选取。 
# 
#  说明： 
# 
#  
#  所有数字（包括 target）都是正整数。 
#  解集不能包含重复的组合。 
#  
# 
#  示例 1： 
# 
#  输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#   [7],
#   [2,2,3]
# ]
#  
#  1 <= candidates.length <= 30 
#  1 <= candidates[i] <= 200 
#  candidate 中的每个元素都是独一无二的。 
#  1 <= target <= 500 
#  
#  Related Topics 数组 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        # 排序，方便之后剪枝
        candidates.sort()
        self.backtrack(candidates, target, [], 0)
        return self.res

    def backtrack(self, candidates, target, path, cal):
        if target == 0:
            self.res.append(path.copy())
            return
        # 从cal开始计数，保证不会出现重复结果
        for i in range(cal, len(candidates)):
            # 剪枝，此处小于0就不用递归了，因为之后的candidates的值都比这个大（排序的作用体现在这里）
            if target - candidates[i] < 0:
                break
            self.backtrack(candidates, target - candidates[i], path + [candidates[i]], i)

# leetcode submit region end(Prohibit modification and deletion)

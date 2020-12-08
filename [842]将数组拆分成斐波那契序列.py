# 给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。 
# 
#  形式上，斐波那契式序列是一个非负整数列表 F，且满足： 
# 
#  
#  0 <= F[i] <= 2^31 - 1，（也就是说，每个整数都符合 32 位有符号整数类型）； 
#  F.length >= 3； 
#  对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。 
#  
# 
#  另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。 
# 
#  返回从 S 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []。 
# 
#  
# 
#  示例 1： 
# 
#  输入："123456579"
# 输出：[123,456,579]
#  
# 
#  示例 2： 
# 
#  输入: "11235813"
# 输出: [1,1,2,3,5,8,13]
#  
# 
#  示例 3： 
# 
#  输入: "112358130"
# 输出: []
# 解释: 这项任务无法完成。
#  
# 
#  示例 4： 
# 
#  输入："0123"
# 输出：[]
# 解释：每个块的数字不能以零开头，因此 "01"，"2"，"3" 不是有效答案。
#  
# 
#  示例 5： 
# 
#  输入: "1101111"
# 输出: [110, 1, 111]
# 解释: 输出 [11,0,11,11] 也同样被接受。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= S.length <= 200 
#  字符串 S 中只含有数字。 
#  
#  Related Topics 贪心算法 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        """回溯"""
        return self.backtrack([], 0, S, 0, 0)

    def backtrack(self, path, S, index, depth):
        # 叶子结点，分割完成
        if depth >= 3 and index == len(S):
            return path.copy()
        if index == len(S):
            return []
        res = []
        for i in range(index, len(S)):
            # 剪枝，index为‘0’只能自己，不能和其他字符连接
            if S[index] == '0' and i > index:
                break
            cur = int(S[index:i + 1])
            # 剪枝
            if cur > 2 ** 31 - 1:
                continue
            # 层数小于2，所有字符串组合均遍历
            if depth < 2:
                tmp = self.backtrack(path + [cur], S, i + 1, depth + 1)
                res = tmp or res
            # 层数大于2，遍历能够符合斐波那契的
            else:
                if cur == path[-1] + path[-2]:
                    tmp = self.backtrack(path + [cur], S, i + 1, depth + 1)
                    res = tmp or res
        return res
        
# leetcode submit region end(Prohibit modification and deletion)

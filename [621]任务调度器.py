# 给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个
# 单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。 
# 
#  然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间（要么执行其他任务，要么待命）
# 
#  你需要计算完成所有任务所需要的 最短时间 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：tasks = ["A","A","A","B","B","B"], n = 2
# 输出：8
# 解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
#      在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。  
# 
#  
#  1 <= task.length <= 104 
#  tasks[i] 是大写英文字母 
#  n 的取值范围为 [0, 100] 
#  
#  Related Topics 贪心算法 队列 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """贪心算法，用数组记录个数，先排个数多的"""
        # 记录每个字母个数
        m = [0] * 26
        for task in tasks:
            m[ord(task) - ord('A')] += 1
        # 按照字母个数升序排序
        m.sort()
        # 完成所有任务最短时间
        res = 0
        # m[-1]是目前个数最多的字母，当还有剩余字母未使用时
        while m[-1] > 0:
            i = 0
            # 两个相同字母间隔为n，每个小循环n+1次
            while i <= n:
                # 当所有字母使用完毕，不用res计数，直接退出
                if m[-1] == 0:
                    break
                    # 当i>26，没有字母填充，待命
                if i < 26 and m[25 - i] > 0:
                    m[25 - i] -= 1
                res += 1
                i += 1
            # 每循环一次，排序一次
            m.sort()
        return res
# leetcode submit region end(Prohibit modification and deletion)

# 请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
#  
# 
#  例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
# 
#  提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。 
#  Related Topics 栈 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def dailyTemperatures(self, tem: List[int]) -> List[int]:
        """
        栈，栈中存的都是没找的更大值的温度
        小于栈顶压栈
        大于栈顶，将栈中所有比其小的都弹出，置res，将自己压栈
        """
        # res初始化，方便按index赋值；如果末尾数为递减，不用额外置0
        stack, res = [0], [0] * len(tem)
        for i in range(1, len(tem)):
            while stack and tem[i] > tem[stack[-1]]:
                res[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
        return res

        
# leetcode submit region end(Prohibit modification and deletion)

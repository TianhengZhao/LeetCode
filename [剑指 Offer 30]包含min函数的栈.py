# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。 
# 
#  
# 
#  示例: 
# 
#  MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.min();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.min();   --> 返回 -2.
#  
# 
#  
# 
#  提示： 
# 
#  
#  各函数的调用总次数不超过 20000 次
#  注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/ 
#  Related Topics 栈 设计


# leetcode submit region begin(Prohibit modification and deletion)
class MinStack:
    """
    要求 min、push 及 pop 的时间复杂度都是 O(1)
    """

    def __init__(self):
        # 使用辅助栈
        self.stack, self.sup = [], []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # 如果x <= self.sup[-1]，x是目前为止stack中最小元素
        if not self.sup or x <= self.sup[-1]:
            self.sup.append(x)

    def pop(self) -> None:
        # stack弹出的元素为最小元素，sup也弹栈
        # sup栈顶元素为stack最小元素
        if self.stack.pop() == self.sup[-1]:
            self.sup.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.sup[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
# leetcode submit region end(Prohibit modification and deletion)

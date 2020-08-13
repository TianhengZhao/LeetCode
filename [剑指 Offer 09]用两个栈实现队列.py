# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的
# 功能。(若队列中没有元素，deleteHead 操作返回 -1 ) 
# 
#  
# 
#  示例 1： 
# 
#  输入：
# ["CQueue","appendTail","deleteHead","deleteHead"]
# [[],[3],[],[]]
# 输出：[null,null,3,-1]
#  
# 
#  示例 2： 
# 
#  输入：
# ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
# [[],[],[5],[2],[],[]]
# 输出：[null,-1,null,null,5,2]
#  
# 
#  提示： 
# 
#  
#  1 <= values <= 10000 
#  最多会对 appendTail、deleteHead 进行 10000 次调用 
#  
#  Related Topics 栈 设计


# leetcode submit region begin(Prohibit modification and deletion)
class CQueue:

    def __init__(self):
        # 栈1正序存放添加的队列元素
        self.stack1 = []
        # 栈2倒序存放原栈1元素
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        # 添加元素时直接加在栈1尾
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        if not self.stack1:
            return -1
        # 栈1元素倒序放入栈2，便于pop
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
# leetcode submit region end(Prohibit modification and deletion)

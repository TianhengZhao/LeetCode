# Dota2 的世界里有两个阵营：Radiant(天辉)和 Dire(夜魇) 
# 他们以一个基于轮为过程的投票进行决定。在每一轮中，每一位参议员都可以行使两项权利中的一项：
#  1.禁止一名参议员的权利：
#  参议员可以让另一位参议员在这一轮和随后的几轮中丧失所有的权利。
#  2.宣布胜利：
#
#  给定一个字符串代表每个参议员的阵营。字母 “R” 和 “D” 分别代表了 Radiant（天辉）和 Dire（夜魇）。然后，如果有 n 个参议员，给定字符
# 串的大小将是 n。 
# 
#  以轮为基础的过程从给定顺序的第一个参议员开始到最后一个参议员结束。这一过程将持续到投票结束。所有失去权利的参议员将在过程中被跳过。 
# 
#  假设每一位参议员都足够聪明，会为自己的政党做出最好的策略，你需要预测哪一方最终会宣布胜利并在 Dota2 游戏中决定改变。输出应该是 Radiant 或 
# Dire。
#  
# 输入："RDD"
# 输出："Dire"
# 解释：
# 第一轮中,第一个来自 Radiant 阵营的参议员可以使用第一项权利禁止第二个参议员的权利
# 第二个来自 Dire 阵营的参议员会被跳过因为他的权利被禁止
# 第三个来自 Dire 阵营的参议员可以使用他的第一项权利禁止第一个参议员的权利
# 因此在第二轮只剩下第三个参议员拥有投票的权利,于是他可以宣布胜利
#
#  给定字符串的长度在 [1, 10,000] 之间. 
#
#  Related Topics 贪心算法


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """双队列"""
        radiant, dire = collections.deque(), collections.deque()
        length = len(senate)
        for i in range(length):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            # 两个队列逐位比较，小的加到队尾后弹出，由于是轮，序号增加；大的直接弹出
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + length)
            else:
                dire.append(dire[0] + length)
            radiant.popleft()
            dire.popleft()
        return 'Radiant' if radiant else 'Dire'
        
# leetcode submit region end(Prohibit modification and deletion)

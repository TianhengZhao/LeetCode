# 给定一个经过编码的字符串，返回它解码后的字符串。 
# 
#  编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。 
# 
#  你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。 
# 
#  此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
#  
# 
#  示例 2： 
# 
#  输入：s = "b3[a2[c]]"
# 输出："baccaccacc"
#
#  Related Topics 栈 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def decodeString(self, s: str) -> str:
        """栈"""
        stack, multi, cur = [], 0, ''
        for char in s:
            if char == '[':
                # 化成树形的话，multi和cur处在同一层
                stack.append([multi, cur])
                multi, cur = 0, ''
            elif char == ']':
                # cur在cur_multi和 same_lavel的下一层，是cur_multi的儿子
                cur_multi, same_lavel = stack.pop()
                cur = same_lavel + cur_multi * cur
            elif 'a' <= char <= 'z':
                cur += char
            # 字符为数字
            else:
                multi = multi * 10 + int(char)
        return cur
# leetcode submit region end(Prohibit modification and deletion)

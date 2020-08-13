# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
#  示例 1： 
# 
#  输入：s = "We are happy."
# 输出："We%20are%20happy."
#  限制： 
# 
#  0 <= s 的长度 <= 10000 



# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def replaceSpace_1(self, s: str) -> str:
        """内置函数"""
        return s.replace(' ', '%20')

    def replaceSpace_2(self, s: str) -> str:
        """
        将字符存入列表
        用join进行拼接
        """
        res = []
        for char in s:
            if char == ' ':
                res.append('%20')
            else:
                res.append(char)
        return ''.join(res)
# leetcode submit region end(Prohibit modification and deletion)

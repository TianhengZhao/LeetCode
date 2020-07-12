# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。
# 
#  所有输入只包含小写字母 a-z 。 
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def longestCommonPrefix_mine(self, strs: List[str]) -> str:
        """
        横向扫描
        前两字符串找出公共前缀pub
        pub与第三个字符串比较找公共子串......
        O(m*n)
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        a = strs[0]
        k = 0
        pub = ""
        while k < len(strs)-1:
            pub = ""
            for i in range(min(len(a), len(strs[k+1]))):
                if a[i] == strs[k+1][i]:
                    pub += a[i]
                if pub == "":
                    return pub
            k += 1
            a = pub
        return pub

    def longestCommonPrefix_other1(self, strs):
        """
        取出列表最大字符串，最小字符串
        二者最长公共前缀即为所有字符串最长公共前缀
        """
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

    def longestCommonPrefix_other2(self, strs):
        """
        将列表中字符串利用zip左对齐纵向压缩成元组
        元组转换成集合，去掉重复字符
        集合中只有一个字符，为公共前缀字符
        """
        ans = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans


# leetcode submit region end(Prohibit modification and deletion)

# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。 
# 
#  字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。 
# 
#  说明：
#  字母异位词指字母相同，但排列不同的字符串。 
#  不考虑答案输出的顺序。 
#  
# 
#  示例 1: 
# 
#  
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#
#  Related Topics 哈希表 


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findAnagramsAns(self, s: str, p: str) -> List[int]:
        # wd是s中窗口的字符及其数量，p_dic是p中字符及其数量
        res, wd, p_dic = [], {}, {}
        for char in p:
            p_dic[char] = p_dic.get(char, 0) + 1
        p_len, s_len = len(p), len(s)
        # left，right是窗口wd的左右界限
        left = right = 0
        while right < s_len:
            cur = s[right]
            # cur不在p_dic中，将窗口清除，窗口左边界在cur下一位
            if cur not in p_dic:
                wd = {}
                left = right = right + 1
            # cur在p_dic中
            else:
                # 将cur添加到窗口中或计数加一
                wd[cur] = wd.get(cur, 0) + 1
                # 若wd大小正好等于目标串p的长度
                if right - left + 1 == p_len:
                    # 比较窗口wd和目标串是否是字母异位
                    if wd == p_dic:
                        res.append(left)
                    # 由于wd满了，要将wd整体右移一位，在wd中清除left位置的字符，left右移一位
                    wd[s[left]] -= 1
                    left += 1
                # 1.wd满了 right右移一位 2.wd未满，要增大窗口，right右移
                right += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)

# 在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，
# 跟随着单词 other(其他)，可以形成新的单词 another(另一个)。 
# 
#  现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。 
# 
#  你需要输出替换之后的句子。 
# 
#  
# 
#  示例： 
# 
#  输入：dict(词典) = ["cat", "bat", "rat"] sentence(句子) = "the cattle was rattled by the battery"
# 输出："the cat was rat by the bat"
#
#  输入只包含小写字母。 
#  1 <= dict.length <= 1000 
#  1 <= dict[i].length <= 100 
#  1 <= 句中词语数 <= 1000 
#  1 <= 句中词语长度 <= 1000 
#  
#  Related Topics 字典树 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:

    def replaceWords(self, dict: List[str], sentence: str) -> str:
        # 字典树初始化
        lookup = {}
        # 向树中插入值; 字典嵌套
        for word in dict:
            tree = lookup
            for ch in word:
                if ch not in tree:
                    tree[ch] = {}
                tree = tree[ch]
            tree['end'] = True

        # 单词前缀判断
        def helper(wo):
            tr = lookup
            for i, al in enumerate(wo):
                if 'end' in tr:
                    # 存在前缀就返回前缀
                    return wo[: i]
                elif al not in tr:
                    # 不存在前缀就跳出循环并返回原词
                    break
                tr = tr[al]
            return wo

        return ' '.join(map(helper, sentence.split(' ')))

# leetcode submit region end(Prohibit modification and deletion)

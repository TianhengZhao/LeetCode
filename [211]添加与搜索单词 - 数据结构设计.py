# 设计一个支持以下两种操作的数据结构： 
# 
#  void addWord(word)
# bool search(word)
#  
# 
#  search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。 
# 
#  示例: 
# 
#  addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#  
# 
#  说明: 
# 
#  你可以假设所有单词都是由小写字母 a-z 组成的。 
#  Related Topics 设计 字典树 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class WordDictionary:

    def __init__(self):
        self.lookup = {}

    def addWord(self, word: str) -> None:
        tree = self.lookup
        for a in word:
            # 如果字典中包含给定键，返回该键对应的值，否则返回为该键设置的值
            tree = tree.setdefault(a, {})
        tree["#"] = {}

    def search(self, word: str) -> bool:
        return self.dfs(word, self.lookup)

    def dfs(self, word, tree):
        """
        对字典树深度优先递归
        :param word: 要查找的单词
        :param tree: 集合
        :return: bool，该单词是否在字典树中
        """
        if not word:
            if "#" in tree:
                return True
            return False
        if word[0] == '.':
            for ch in tree:
                if self.dfs(word[1:], tree[ch]):
                    return True
        elif word[0] in tree:
            if self.dfs(word[1:], tree[word[0]]):
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# leetcode submit region end(Prohibit modification and deletion)

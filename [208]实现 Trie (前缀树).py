# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。 
# 
#  示例: 
# 
#  Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");   
# trie.search("app");     // 返回 true 
# 
#  说明: 
# 
#  
#  你可以假设所有的输入都是由小写字母 a-z 构成的。 
#  保证所有输入均为非空字符串。 
#  
#  Related Topics 设计 字典树


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class TrieNode:
    """结点类"""
    def __init__(self):
        # defaultdict 当key不存在时，返回的是TrieNode的默认值
        # 将一个结点的所有孩子存放于一个字典中
        self.children = defaultdict(TrieNode)
        # 记录当前单词是否结束
        self.word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for w in word:
            cur = cur.children[w]

        cur.word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        if cur.word:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for p in prefix:
            if p not in cur.children:
                return False
            cur = cur.children[p]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# leetcode submit region end(Prohibit modification and deletion)

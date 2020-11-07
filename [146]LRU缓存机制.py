# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制 。 
# 
#  
#  
#  实现 LRUCache 类： 
# 
#  
#  LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存 
#  int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。 
#  void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上
# 限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。 
#  
# 
#  
#  
#  
# 
#  进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？ 
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 3000 
#  0 <= value <= 104 
#  最多调用 3 * 104 次 get 和 put 
#  
#  Related Topics 设计


# leetcode submit region begin(Prohibit modification and deletion)
class listNode:

    def __init__(self, key=None, value=None):
        # 双向链表 保存key:value键值对
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # 使用哈希表+双向链表的数据结构
        self.dic = {}
        self.capacity = capacity
        # 空的头和尾结点，便于操作
        self.sen = listNode()
        self.tail = listNode()
        self.sen.next = self.tail
        self.tail.pre = self.sen

    def move_to_tail(self, key):
        """
        将key对应的结点移到双向链表尾
        """
        node = self.dic[key]
        # 脱离原位置
        node.next.pre = node.pre
        node.pre.next = node.next
        # 插入到末尾位置
        self.tail.pre.next = node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node

    def get(self, key: int) -> int:
        if key in self.dic:
            # 最近访问过该节点，将该节点移到双向链表尾
            self.move_to_tail(key)
            return self.dic[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 如果哈希表中存在此键值
        if key in self.dic:
            # 最近访问过该节点，将该节点移到双向链表尾
            self.move_to_tail(key)
            # 并且更新其value值
            self.dic[key].value = value
        # 哈希表中无此键值，将其加入到哈希表中
        else:
            # 哈希表如果已满
            if self.capacity == len(self.dic):
                # 在哈希表中删除双向链表表头元素，也就是最不常用节点
                self.dic.pop(self.sen.next.key)
                # 在双向链表中删除表头元素
                self.sen.next = self.sen.next.next
                self.sen.next.pre = self.sen
            # 将新key值加入到哈希表中
            node = listNode(key, value)
            self.dic[key] = node
            # 插入双向链表尾
            self.tail.pre.next = node
            node.pre = self.tail.pre
            node.next = self.tail
            self.tail.pre = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)

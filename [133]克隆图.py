# 给你无向 连通 图中一个节点的引用，
# 遍历整个图
# 请你返回该图的 深拷贝（克隆）。
#
# 简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。
# 该图在测试用例中使用邻接列表表示。
# 
#  给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。
#  
#  节点数不超过 100 。 
#  每个节点值 Node.val 都是唯一的，1 <= Node.val <= 100。 
#  无向图是一个简单图，这意味着图中没有重复的边，也没有自环。 
#  由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居。 
#  图是连通图，你可以从给定节点访问到所有节点。 
#  
#  Related Topics 深度优先搜索 广度优先搜索 图


# leetcode submit region begin(Prohibit modification and deletion)

# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def __init__(self):
        # 字典，存放访问过的结点，key是原图的结点，value为其克隆结点
        # 避免相邻结点死循环
        self.visited = {}

    def cloneGraph(self, node):
        """
        深度优先遍历，递归
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node

        # 如果该节点被访问过，返回克隆后的结点
        if node in self.visited:
            return self.visited[node]

        # 建立node的克隆结点
        clone_node = Node(node.val, [])

        # 将node加入已访问字典
        self.visited[node] = clone_node

        # 将node的邻居结点一个个复制给克隆结点
        for n in node.neighbors:
            clone_node.neighbors.append(self.cloneGraph(n))

        # 返回克隆结点
        return clone_node

    def cloneGraph_2(self, node):
        """
        广度优先，迭代
        """
        if not node:
            return node
        visited = {}
        queue = deque([node])
        # 结点在入队之前加入visited
        visited[node] = Node(node.val, [])

        while queue:
            cur_node = queue.popleft()
            # 出队后遍历每个邻接节点
            for neighbor in cur_node.neighbors:
                # 若该邻接节点未被访问过
                if neighbor not in visited:
                    # 1、在visited里为该邻接节点建个位置
                    visited[neighbor] = Node(neighbor.val, [])
                    # 入队
                    queue.append(neighbor)
                # 2、复制该邻接节点到clone的邻接列表里
                visited[cur_node].neighbors.append(visited[neighbor])

        return visited[node]
        
# leetcode submit region end(Prohibit modification and deletion)

# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。 
# 
#  在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1] 
# 
#  给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
# 
#  示例 1: 
# 
#  输入: 2, [[1,0]] 
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。 
# 
#  示例 2: 
# 
#  输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。 
# 
#
#  
#  输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。 
#  你可以假定输入的先决条件中没有重复的边。 
#  1 <= numCourses <= 10^5 
#  
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinishAns(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        拓扑排序 判断图是否是有向无环图
        记录顶点的入度及其邻接表
        将所有入度为0的顶点入队
        出队，删除该顶点，然后将所有入度为0的顶点再入队
        最后图中还有顶点就有环
        """
        indegrees = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]
        # 统计所有顶点入度和邻接表
        for start, end in prerequisites:
            indegrees[end] += 1
            adjacency[start].append(end)
        que = deque()
        # 所有入度为0的顶点入队
        for i in range(numCourses):
            if not indegrees[i]:
                que.append(i)
        while que:
            cur = que.popleft()
            # 每‘删除’一个顶点，总顶点值减一
            numCourses -= 1
            # cur的邻接表中所有顶点入度减一，若有为0的，入队
            for adj in adjacency[cur]:
                indegrees[adj] -= 1
                if not indegrees[adj]:
                    que.append(adj)
        return not numCourses
# leetcode submit region end(Prohibit modification and deletion)

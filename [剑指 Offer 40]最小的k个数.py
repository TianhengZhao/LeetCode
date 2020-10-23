# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
#  
# 
#  示例 2： 
# 
#  输入：arr = [0,1,2,1], k = 1
# 输出：[0] 
# 
#  
# 
#  限制： 
# 
#  
#  0 <= k <= arr.length <= 10000 
#  0 <= arr[i] <= 10000 
#  
#  Related Topics 堆 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
import heapq
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        end = len(arr)
        for i in range(end // 2, -1, -1):
            # end是不算在内的
            self.sink(arr, i, end)
        for i in range(end - 1, end - k - 1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.sink(arr, 0, i)
        return arr[end - k:]

    def sink(self, arr, startpos, endpos):
        # 记录，否则之后会改变
        target = arr[startpos]
        childpos = startpos * 2 + 1
        tmppos = startpos
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and arr[rightpos] <= arr[childpos]:
                childpos = rightpos
            if arr[childpos] < target:
                arr[tmppos] = arr[childpos]
                tmppos = childpos
                childpos = tmppos * 2 + 1
            else:
                break
        arr[tmppos] = target

    def getLeastNumbers_ans(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()
        # 加上负号 绝对值变成大根堆
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            # hp里存放前k个小的数
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans

# leetcode submit region end(Prohibit modification and deletion)

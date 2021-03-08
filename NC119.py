# 最小的K个数

import queue

class Solution:
    # 大根堆
    def getLeastNumbers(self,arr,k):
        q=queue.PriorityQueue()
        for i,j in enumerate(arr):
            if q.qsize()<k:
                q.put((-j,j))
                continue
            if j<q.queue[0][1]:
                q.get()
                q.put((-j,j))
        return list(map(lambda x:x[1],q.queue))

    # 分区法:利用快速排序中的分区函数
    def getLeastNumbers1(self,arr,k):
        length = len(arr)
        l = 0
        r = length - 1
        if k > length or k <= 0:
            return []
        if k == length:
            return sorted(arr)
        while l < r:
            m = self.part(arr, l, r)
            if m + 1 > k:
                r = m
            elif m + 1 < k:
                l = m + 1
            else:
                return sorted(arr[0:m + 1])

    def part(self, arr, i, j):
        pivot = arr[i]
        l = i + 1
        r = j
        while l <= r:
            if arr[l] < pivot:
                l += 1
            else:
                arr[l], arr[r] = arr[r], arr[l]
                r -= 1
        arr[i], arr[r] = arr[r], arr[i]
        return r


if __name__ == '__main__':
    arr=[4,5,1,6,2,7,3,8]
    r=Solution().getLeastNumbers1(arr,8)
    print(r)


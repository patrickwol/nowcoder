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

    # 快速排序分区法
    def getLeastNumbers1(self,arr,k):
        m=self.part(arr,0,len(arr)-1)
        while True:
            if m+1>k:
                m=self.part(arr,0,m)
            elif m+1<k:
                m=self.part(arr,m+1,len(arr)-1)
            else:
                break
        return arr[0:m+1]

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
    arr=[1,3,3,0,4,2,5]
    r=Solution().getLeastNumbers1(arr,4)
    print(r)


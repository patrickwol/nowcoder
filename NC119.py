# 最小的K个数

import queue


class Solution:
    # 大根堆
    def getLeastNumbers(self, arr, k):
        q = queue.PriorityQueue()
        for i, j in enumerate(arr):
            if q.qsize() < k:
                q.put((-j, j))
                continue
            if j <= q.queue[0][1]:
                q.get()
                q.put((-j, j))
        return list(map(lambda x: x[1], q.queue))

    # 分区法:利用快速排序中的分区函数
    def getLeastNumbers1(self, arr, k):
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

    # 自己实现大根堆
    def getLeastNumbers2(self, arr, k):
        q = []
        for i, j in enumerate(arr):
            if len(q) < k:
                self.shiftUp(q, j)
                continue
            if q[0] >= j:
                self.poll(q)
                self.shiftUp(q, j)
        return q

    def shiftUp(self, q, v):
        q.append(v)
        if len(q) == 0:
            return q
        k = len(q) - 1
        while k > 0:
            if q[k] > q[(k - 1) // 2]:
                q[k], q[(k - 1) // 2] = q[(k - 1) // 2], q[k]
            else:
                return q
            k = (k - 1) // 2
        return q

    def shiftDown(self, q):
        k = 0
        half = (len(q) - 2) / 2 # 非叶子节点最大下标
        while k <= half:
            childLeft = k * 2 + 1
            rightRight = childLeft + 1
            t = childLeft  # 较大值的下标
            if rightRight < len(q) - 1 and q[childLeft] < q[rightRight]:
                t = rightRight
            if q[k] < q[t]:
                q[k], q[t] = q[t], q[k]
                k = t
            else:
                break
        return q

    def poll(self, q):
        q[0] = q[len(q) - 1]
        q.pop()
        self.shiftDown(q)
        return q


if __name__ == '__main__':
    arr = [4, 5, 1, 6, 2, 7, 3, 8]
    r = Solution().getLeastNumbers2(arr, 6)
    print(r)
    arr1 = [4, 5, 1, 6, 2, 7, 3, 8]
    d = Solution().getLeastNumbers(arr1, 6)
    print(d)

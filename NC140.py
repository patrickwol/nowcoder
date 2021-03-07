# 排序

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 将给定数组排序
# @param arr int整型一维数组 待排序的数组
# @return int整型一维数组
#
class Solution:
    def MySort(self, arr):
        # self.quickSort(arr, 0, len(arr) - 1)
        self.mergeSort(arr, 0, len(arr) - 1)
        return arr

    def quickSort(self, arr, i, j):
        if i < j:
            # m = self.part(arr, i, j)
            # self.quickSort(arr, i, m - 1)
            # self.quickSort(arr, m + 1, j)

            a, b = self.part2(arr, i, j)
            self.quickSort(arr, i, a)
            self.quickSort(arr, b, j)

    # 单方向扫描分区
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

    # 双向扫描分区法
    def part1(self, arr, i, j):
        pivot = arr[i]
        l = i + 1
        r = j
        while l <= r:
            while l <= r and arr[l] <= pivot:
                l += 1
            while l <= r and arr[r] > pivot:
                r -= 1
            if l < r:
                arr[l], arr[r] = arr[r], arr[l]
        arr[i], arr[r] = arr[r], arr[i]
        return r

    # 三指针分区法：适用于相同值较多的情况
    def part2(self, arr, i, j):
        pivot = arr[i]
        l = i + 1
        m = i + 1
        r = j
        while l <= r:
            if arr[l] < pivot:
                if arr[l] != arr[m]:
                    arr[l], arr[m] = arr[m], arr[l]
                l += 1
                m += 1
            elif arr[l] > pivot:
                arr[l], arr[r] = arr[r], arr[l]
                r -= 1
            else:
                l += 1
        arr[i], arr[m - 1] = arr[m - 1], arr[i]
        return m - 2, r + 1

    # 归并排序
    def mergeSort(self, arr, i, j):
        if i < j:
            m = (i + j) // 2
            self.mergeSort(arr, i, m)
            self.mergeSort(arr, m + 1, j)
            self.merge(arr, i, m, m + 1, j)

    def merge(self, arr, i, j, l, r):
        a=i
        length = (j - i + 1) + (r - l + 1)
        tmp = [None] * length
        p = 0
        while i <= j and l <= r:
            if arr[i] <= arr[l]:
                tmp[p] = arr[i]
                i += 1
            else:
                tmp[p] = arr[l]
                l += 1
            p += 1
        while i <= j:
            tmp[p] = arr[i]
            p += 1
            i += 1
        while l <= r:
            tmp[p] = arr[l]
            p += 1
            l += 1
        arr[a:r+1] = tmp[:]


if __name__ == '__main__':
    array = [5,5,3,2,9,1,7]
    print(Solution().MySort(array))

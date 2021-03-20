# 合并两个有序的数组
#
# @param A int整型一维数组
# @param B int整型一维数组
# @return void
#
class Solution:
    def merge(self, A, m, B, n):
        a, b = m - 1, n - 1
        while a >= 0 and b >= 0:
            if A[a] > B[b]:
                A[a + b + 1] = A[a]
                a -= 1
            else:
                A[a + b + 1] = B[b]
                b -= 1
        if b >= 0:
            A[:b+1] = B[:b+1]


if __name__ == '__main__':
    A = [5, 7, 9]
    m= len(A)
    B = [2, 3, 6, 8, 10]
    A.extend([None] * len(B))
    Solution().merge(A, m, B, len(B))
    print(A)

# 两数之和
#
# @param numbers int整型一维数组
# @param target int整型
# @return int整型一维数组
#
class Solution:
    def twoSum(self, numbers, target):
        d = {}
        res = []
        for i, j in enumerate(numbers):
            if j in d:
                res.append(d[j] + 1)
                res.append(i + 1)
                return res
            d[target - j] = i
        return res


if __name__ == '__main__':
    list = [20, 70, 110, 150]
    res = Solution().twoSum(list, 220)
    print(res)

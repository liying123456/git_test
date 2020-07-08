# leetcode_149 number math
# 直线上最多的点数
from collections import defaultdict
from decimal import Decimal


def maxPoints(points):
    """
    两点确定斜率，遍历所有点，计算点与point的斜率，
    斜率相同证明在一条直线上
    :param points: 点坐标
    :return:
    """
    if len(points) < 3:
        return len(points)
    dct = defaultdict(int)  # {斜率：该直线上最多的点数}
    result = 0  # 记录最终结果
    for index, point1 in enumerate(points):
        same_num = 1
        dct.clear()
        for _, point2 in enumerate(points[index+1:]):
            # 存在相同点的情况
            if point1 == point2:
                same_num = same_num + 1
                continue
            # 当横坐标一致时
            elif point1[0] == point2[0] and point1[1] != point2[1]:
                k = float('inf')  # 正无穷
            else:
                y = Decimal(point2[1] - point1[1])
                x = Decimal(point2[0] - point1[0])
                k = y / x
            dct[k] = dct[k] + 1
        if result < same_num:
            result = same_num
        for _, val in dct.items():
            if val + same_num > result:
                result = val + same_num
    return result


if __name__ == '__main__':
    a = [[1,1],[2,2],[3,3]]
    b = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(maxPoints(a))
    print(maxPoints(b))
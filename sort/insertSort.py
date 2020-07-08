# 插入排序
# 时间复杂度， 最坏情况， 最好情况,   空间复杂度
#  O(n^2),     O(n^2),    O(n)，     O(1)
def insert_sort(ls):
    """
    从第二个元素开始遍历，作为当前元素，放入一个临时变量存放
    以当前元素开始，向前扫描，直到找到比该元素更小的元素或到达第一个元素
    :param ls:
    :return:
    """
    for item in range(1, len(ls)):
        j = item - 1
        # 当前元素小于前一个元素时，临时变量存放当前元素，前面的元素后移一位
        if ls[item] < ls[j]:
            tmp = ls[item]
            ls[item] = ls[j]
            j = j - 1
            # 继续向前搜索，一旦tmp小于这些元素，将他们后移，知道找到一个小于tmp的元素或到最左
            while j >= 0 and tmp < ls[j]:
                ls[j+1] = ls[j]
                j = j - 1
            # 将临时变量放在合适的位置
            ls[j+1] = tmp
    return ls


if __name__ == "__main__":
    a = [4, 7, 8, 3, 5, 9]
    print(insert_sort(a))
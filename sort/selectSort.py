# 选择排序
# 时间复杂度， 最坏情况， 最好情况,   空间复杂度
#  O(n^2),     O(n^2),    O(n^2)，    O(1)
def select_sort(ls):
    """
    从左到右遍历数组
    取未排序序列的首位作为开始，与后面的元素作对比，
    找到未排序序列中的最小元素，并放在该序列的首位（最小元素与首位元素交换位置）
    因此需要两个变量来记录，当前最小元素的值，以及他的索引号
    :param ls:
    :return:
    """
    for item in range(len(ls)):
        min = ls[item]
        min_index = item  # 最小元素的索引
        for j in range(item+1, len(ls)):
            if min > ls[j]:
                min = ls[j]
                min_index = j
        ls[item], ls[min_index] = ls[min_index], ls[item]
    return ls


if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print(select_sort(a))
    b = [64, 34, 25, 12, 22, 11, 90]
    print(select_sort(b))
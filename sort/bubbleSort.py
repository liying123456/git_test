# 冒泡排序
# 时间复杂度， 最坏情况， 最好情况,   空间复杂度
#  O(n^2),     O(n^2),    O(n)，     O(1)
def bubble_sort(ls):
    """
    从左到右扫描元素
    每一趟，相邻元素进行对比,如果顺序相反，颠倒一下
    :param ls:
    :return:
    """
    for item in range(len(ls)):
        ex_flag = False  # 改进版本，添加一个标志位，True表示当前序列还需要进行交换位置，并不是一个有序的。
        for j in range(0, len(ls)-item-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
                ex_flag = True
            if not ex_flag:
                return ls
    return ls


if __name__ == "__main__":
    a = [4, 7, 8, 3, 5, 9]
    print(bubble_sort(a))
    b = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(b))
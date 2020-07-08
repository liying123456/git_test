# 快速排序
# 时间复杂度， 最坏情况， 最好情况,   空间复杂度
#  O(nlogn),   O(n^2),    O(nlogn)，  O(nlogn)
def quick_sort(arr, low, high):
    """
    分治的思想，
    选择一个数作为基准，将数组分为两部分，一部分全部小于基准，一部分全部大于基准
    递归进行
    :param ls:
    :return:
    """
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)
    return arr


def partition(arr, low, high):
    """
    分治函数
    设置一个基准，
    重新排列数组，所有比基准小德数都排在基准之前
    :param arr:
    :param low:
    :param high:
    :return:
    """
    i = low-1  # 记录分裂位置的索引
    pivot = arr[high]  # 基准值
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


if __name__ == "__main__":
    a = [4, 7, 8, 3, 5, 9]
    print(quick_sort(a, 0, len(a)-1))
    b = [64, 34, 25, 12, 22, 11, 90]
    print(quick_sort(b, 0, len(b)-1))
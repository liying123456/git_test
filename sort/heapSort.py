# 堆排序
# 时间复杂度， 最坏情况， 最好情况,   空间复杂度
#  O(nlogn),  O(nlogn),  O(nlogn)，   O(1)
# 类似于选择排序，但是是用二叉树结构存放数据
# 每一次选出最小的元素放到未排序的首位


def heap_sort(ls):
    """
    首先建堆
    然后将堆顶元素与最后一个元素交换位置，并将堆顶元素输出
    调整堆
    再循环
    直到堆为空
    :param ls:
    :return:
    """
    if len(ls) <= 1:
        return ls

    def adjust_heap(arr, length, parent):
        """
        按照上浮和下沉调整堆。
        大根堆，堆顶元素为最大
        :param arr:
        :param length:
        :param parent:
        :return:
        """
        tmp = arr[parent]
        child = 2 * parent + 1  # left child
        # i节点是一个中间节点，存在左孩子
        while child < length:
            # 如果有右孩子，且右孩子大于左孩子，定位到右孩子
            if child + 1 < length and arr[child + 1] > arr[child]:
                child = child + 1
            # 如果父节点大于子节点，则跳过
            if arr[child] >= arr[parent]:
                arr[parent] = arr[child]
                parent = child
                child = 2 * child + 1
            else:
                break
        arr[parent] = tmp

    # 建堆，并调整
    for i in range(len(ls)//2-1, -1, -1):
        adjust_heap(ls, len(ls), i)
    # 弹出堆顶元素（最大的元素,ls[0]）,  ls[item]是末尾元素
    for item in range(len(ls)-1, 0, -1):
        ls[item], ls[0] = ls[0], ls[item]
        adjust_heap(ls, item, 0)
    return ls


if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print(heap_sort(a))
    b = [64, 34, 25, 12, 22, 11, 90]
    print(heap_sort(b))
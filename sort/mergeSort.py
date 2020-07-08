# 合并排序
# 时间复杂度， 最坏情况， 最好情况,   空间复杂度
#  O(nlogn),   O(nlogn),   O(nlogn)，  O(n)
def merge(l, r):
    """
    合并的过程
    :param l:
    :param r:
    :return:
    """
    new_list = []
    tag_l = 0
    tag_r = 0
    while tag_l < len(l) and tag_r < len(r):
        if l[tag_l] < r[tag_r]:
            new_list.append(l[tag_l])
            tag_l = tag_l + 1
        else:
            new_list.append(r[tag_r])
            tag_r = tag_r + 1
    if tag_l == len(l):
        for i in r[tag_r:]:
            new_list.append(i)
    elif tag_r == len(r):
        for j in l[tag_l]:
            new_list.append(j)
    return new_list


def merge_sort(ls):
    """
    归并排序，先拆分再合并
    拆分过程
    递归
    :param ls:
    :return:
    """
    if len(ls) <= 1:
        return ls
    middle = int(len(ls) / 2)
    left = merge_sort(ls[:middle])
    right = merge_sort(ls[middle:])
    return merge(left, right)


if __name__ == "__main__":
    a = [4, 7, 8, 3, 5, 9]

    print(merge_sort(a))
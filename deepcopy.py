# 深拷贝的实现
#id()内置函数用于返回对象的内存地址
import copy


def deepcopy(copls):
    if isinstance(copls, list):
        li = []
        for item in copls:
            li.append(deepcopy(item))
        return li
    elif isinstance(copls, tuple):
        li = []
        for i in copls:
            li.append(deepcopy(i))
        return li
    elif isinstance(copls, dict):
        dct = {}
        for k, v in copls.items():
            dct[k] = deepcopy(v)
        return dct
    else:
        return copls


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, ([5, 6, 7, [7, 8, {'abc': 8975, 'dex': 123, 'v': 'vvvv'}, 5, 4, 7]], (2, 5, {'z:2'}))]
    res = deepcopy(lst)
    print(lst)
    print(res)
    print('deep\n', id(res[5][0]))
    print('lst\n', id(lst[5][0]))
    ls = copy.copy(lst)
    print('ls\n', id(ls[5][0]))

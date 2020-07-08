# 深拷贝与浅拷贝
import copy


if __name__ == '__main__':
    a = [1,2,3,4]
    a1 = [1,2,3,4,[11,22,33]]
    b = copy.copy(a)
    b1 = copy.copy(a1)
    b2 = a1[:]
    b3 = a1
    a.append(5)
    a1.append(5)
    a1[4].append(55)
    print(a)
    print(b)
    print('--------------')
    print(a1)
    print(b1)
    print(b2)
    print(b3)
    print(id(a1))
    print(id(b3))
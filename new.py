while 1:
    ls = []
    new = []
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    for i in input().split():
        ls.append(int(i))
    for j in input().split():
        ls.append(int(j))
    new = sorted(set(ls))
    # for z in new:
    #     print(z, end=' ')
    s = ''
    for z in new:
        s = str(z) + ' '
    print(s)
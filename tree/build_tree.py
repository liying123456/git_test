# 从一个列表，构建一个完全二叉树

class TreeNode:
    """
    定义树节点
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    """
    用于构建一个二叉树
    """
    lt = []  # 依次存放左右孩子未满的节点
    def __init__(self):
        self.root = None
    def add(self, number):
        """
        将节点添加到二叉树中，构建一个二叉树
        但该函数添加节点是从上到下，从左到右添加节点。完全二叉树
        :param number: 节点的值
        :return:
        """
        node = TreeNode(number)
        if self.root == None:
            self.root = node
            Tree.lt.append(self.root)
        else:
            while True:
                # 依次给左右孩子未满的节点分配孩子
                point = Tree.lt[0]
                # 左孩子
                if point.left == None:
                    point.left = node
                    Tree.lt.append(point.left)
                # 右孩子
                elif point.right == None:
                    point.right = node
                    Tree.lt.append(point.right)
                    Tree.lt.pop(0)  # 将已拥有左右孩子的节点从列表中删去
                    return
l1 = [1,3,2,5]
t1 = Tree()
for i in l1:
    t1.add(i)
l2 = [2,1,3,4]
t2 = Tree()
for j in l2:
    t2.add(j)
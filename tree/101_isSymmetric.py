# leetcode 101 对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。
# 该程序中包含了构建树的函数，科科

# 例如，二叉树[1, 2, 2, 3, 4, 4, 3]
# 是对称的。
#       1
#     /   \
#   2      2
# /  \    / \
# 3  4   4   3
#
# 但是下面这个[1, 2, 2, null, 3, null, 3]
# 则不是镜像对称的:
#   1
# /   \
# 2    2
#  \    \
#   3    3

class TreeNode:
    """
    定义树节点
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bulid_tree(root, ls):
    """
    将节点添加到二叉树中，构建一个二叉树
    但该函数添加节点是从上到下，从左到右添加节点。完全二叉树
    :param ls: 数组，节点的值
    :return:
    """
    lt = []  # 用于放未拥有左右孩子的节点
    lt.append(root)
    for i in range(1, len(ls)):
        # 依次给左右孩子未满的节点分配孩子
        point = lt[0]
        # 左孩子
        if point.left == None:
            point.left = TreeNode(ls[i])
            lt.append(point.left)
        # 右孩子
        elif point.right == None:
            point.right = TreeNode(ls[i])
            lt.append(point.right)
            lt.pop(0)  # 将已拥有左右孩子的节点从列表中删去
    return root


class Solution:
    def is_symmetric_1(self, root: TreeNode) -> bool:
        """
        递归法判断是不是镜像二叉树
        分支法，看左子树和右子树是不是相等的
        :param root:
        :return:
        """
        if root == None:
            return True
        else:
            return self.judge(root.left, root.right)

    def judge(self, left, right):
        """
        递归法判断左右节点是否对称,
        左节点的右孩子和右节点的左孩子是否相等    左节点的左孩子和右节点的右孩子是否想等
        :param left:
        :param right:
        :return:
        """
        if left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif left == None and right == None:
            return True
        elif left.val != right.val:
            return False
        else:
            return self.judge(left.right, right.left) and self.judge(left.left, right.right)

    def is_symmetric_2(self, root: TreeNode) -> bool:
        """
        迭代法判断对称
        利用列表存放待比较的左右节点。
        每次从列表中取出一对进行比较。如果相等，将他们的子节点按照顺序放入列表
        :param root:
        :return:
        """
        if root == None:
            return True
        nodeList = [root.left, root.right]  # 用于存在待比较的左右节点
        while nodeList:
            left = nodeList.pop(0)
            right = nodeList.pop(0)
            if left == None and right != None:
                return False
            elif left != None and right == None:
                return False
            elif left == None and right == None:
                continue
            elif left.val != right.val:
                return False
            # 注意放入数组的顺序，代表了比较顺序。
            nodeList.append(left.left)
            nodeList.append(right.right)
            nodeList.append(left.right)
            nodeList.append(right.left)
        return True



t1 = [1,2,2,0,3,0,3]
r1 = TreeNode(t1[0])
root1 = bulid_tree(r1, t1)
sol = Solution()
print(sol.is_symmetric_2(root1))
t2 = [1,2,2,3,4,4,3,5,6,7,8,8,7,6,5]





# leetcode_543 二叉树的直径

# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
#
#
#
# 示例:
# 给定二叉树
#
#       1
#      / \
#     2    3
#    / \
#   4   5
#
# 返回 3, 它的长度是路径[4, 2, 1, 3]或者[5, 2, 1, 3]。
#
# 注意：两结点之间的路径长度是以它们之间边的数目表示。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(root, ls):
    """
    创建二叉树
    :param root:
    :param ls:
    :return:
    """
    if root == None:
        return root
    lt = []
    lt.append(root)
    for i in ls[1:]:
        pointer = TreeNode(i)
        if lt[0].left == None:
            lt[0].left = pointer
            lt.append(pointer)
        elif lt[0].right == None:
            lt[0].right = pointer
            lt.pop(0)
            lt.append(pointer)
    return root


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode)->int:
        """
        递归循环，得出经过该节点的最大路径长度
        :param root:
        :return:
        """
        if root == None:
            return 0
        self.result = 0 # 存放最大的路径长度
        def treemax(tree):
            """
            循环得出经过该节点的最大路径长度
            :param root:
            :return:
            """
            if tree == None:
                return 0
            l = treemax(tree.left)
            r = treemax(tree.right)  # 得到右子树的深度-1
            self.result = max(l+r+1, self.result)  # 这是经过节点tree的最大路径长度
            return max(l, r) + 1
        treemax(root)
        return self.result-1

l1 = [1,2,3,4,5]
root = TreeNode(l1[0])
tree1 = build_tree(root, l1)
sol = Solution()
retult = sol.diameterOfBinaryTree(tree1)
print(retult)




# leetcode 226翻转一个二叉树
# 输入：
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
# 输出：
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(root, ls):
    """
    构建一个二叉树
    :param root:
    :param ls:
    :return:
    """
    if root is None:
        return root
    lt = []
    lt.append(root)
    for i in ls[1:]:
        pointer = lt[0]
        node = TreeNode(i)
        if pointer.left == None:
            pointer.left = node
            lt.append(node)
        elif pointer.right == None:
            pointer.right = node
            lt.pop(0)
            lt.append(node)
    return root


class Solution:
    def invertTree(self, root:TreeNode)->TreeNode:
        """
        翻转二叉树
        分治，递归，
        先递归完成左子树和右子树子节点的转换，
        最后将左子树放在根节点的右边，右子树放在根节点的左边
        :param root:
        :return:
        """
        if root is None:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.right = left
        root.left = right
        return root


l1 = [4,2,7,1,3,6,9]
r = TreeNode(l1[0])
root = build_tree(r, l1)
sol = Solution()
result = sol.invertTree(root)



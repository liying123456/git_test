# leetcode 98 中等 判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
#     节点的左子树只包含小于当前节点的数。
#     节点的右子树只包含大于当前节点的数。
#     所有左子树和右子树自身必须也是二叉搜索树。
#
# 示例 1:
#
# 输入:
#     2
#    / \
#   1   3
# 输出: true
#
# 示例 2:
#
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。


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

    def isValidBST_1(self, root:TreeNode)->bool:
        """
        递归法判断二叉树
        注意：空的根节点也是一个标准二叉树
        :param root:
        :return:
        """
        if root is None:
            return True
        return self.valid(root, -2**32, 2**32)

    def valid(self, root:TreeNode, small, large)->bool:
        """
        递归法
        对于每一个节点，左孩子小于他，右孩子大于他
        且，左子树所有的值都要小于他，相当于左子树有一个上界。
        右子树所有值要大于他，相当于右子树有一个下界。
        :param root:
        :param small: 下界，左子树应该大于他
        :param large:上界， 右子树应该小于他
        :return:
        """
        if root is None:
            return True
        if small < root.val < large:
            return self.valid(root.left, small, root.val) and self.valid(root.right, root.val, large)
        return False

    def isValidBST_2(self, root:TreeNode)->bool:
        """
        中序遍历二叉树，如果结果是递增的则是合格二叉树
        中序：左，根，右
        :param root:
        :return:
        """
        raw_list = self.search(root)
        if raw_list != sorted(list(set(raw_list))):  # set的作用是去掉所有重复元素，一个合格的二叉树中，父节点和子节点不会相等
            return False
        return True

    def search(self, node:TreeNode):
        """
        中序遍历
        :param node:
        :return:
        """
        if node == None:
            return []
        res = []
        res = res + self.search(node.left)
        res.append(node.val)
        res = res + self.search(node.right)
        return res



l1 = [2,1,3]
r = TreeNode(l1[0])
root = build_tree(r, l1)
sol = Solution()
result = sol.isValidBST_1(root)
print(result)

l2 = [5,1,4,0,0,3,6]
r = TreeNode(l2[0])
root = build_tree(r, l2)
sol = Solution()
result = sol.isValidBST(root)
print(result)
# leetcode 538 二叉搜索树转换为累加树

# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
#
# 例如：
#
# 输入: 原始二叉搜索树:
#       5
#      / \
#     2   13
#
# 输出: 转换为累加树:
#       18
#       / \
#     20  13
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
    def convertBST(self, root: TreeNode)->TreeNode:
        """
        利用二叉树的性质（右子树大于中间节点，大于左子树节点）
        因此按照右中左的顺序遍历，依次累加
        :param root:
        :return:
        """
        if root == None:
            return root
        self.s = 0  # 记录当前应该加的数

        def search(node):
            """
            右中左遍历树,
            :param node:
            :return:
            """
            if node == None:
                return
            search(node.right)
            node.val = node.val + self.s
            self.s = node.val
            search(node.left)
        search(root)
        return root

l1 = [5,2,13]
ro = TreeNode(l1[0])
tree1 = build_tree(ro, l1)
sol = Solution()
result = sol.convertBST(tree1)
print("1")

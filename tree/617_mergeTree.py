# leetcode 617
# 合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
# 必须从两个树的根节点开始合并
# 输入:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# 输出:
# 合并后的树:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7


class TreeNode:
    """
    定义树节点
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def merge_tree(self, t1:TreeNode, t2:TreeNode)->TreeNode:
        """
        从两个树的根节点
        :param t1:
        :param t2:
        :return:
        """
        if t1 == None:
            return t2
        elif t2 == None:
            return t1
        else:
            t1.val = t1.val + t2.val
            t1.left = self.merge_tree(t1.left, t2.left)
            t1.right = self.merge_tree(t1.right, t2.right)
            return t1

# 手动构造一个二叉树
root1 = TreeNode(1)
n1 = TreeNode(3)
root1.left = n1
n2 = TreeNode(2)
root1.right = n2
n1.left = TreeNode(5)

root2 = TreeNode(2)
n3 = TreeNode(1)
n4 = TreeNode(3)
n5 = TreeNode(0)
n6 = TreeNode(4)
root2.left = n3
root2.right = n4
n3.left = n5
n3.right = n6

sol = Solution()
new_tree = sol.merge_tree(root1, root2)
print(new_tree)

# leetcode 96, 中等， 动态规划的思想
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
# 示例:
#
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
import math


class Solution:
    def numTrees_1(self, n:int)->int:
        """
        利用动态规划的思想从底向上解答问题。
        假设有m种二叉树，m = 左子树的种类 * 右子树的种类
        因此可以形成一个表达式num(n) = num(j) * num(n-j-1)
        注意当根节点为空时，也是一种二叉树，
        :param n:
        :return:
        """
        re = [0 for i in range(0, n+1)]  # 注意这里是n+1,
        re[0] = 1  #  0时算一个树
        re[1] = 1
        for i in range(2, n+1):
            for j in range(0, i):
                re[i] = re[i] + re[j] * re[i-j-1]
        return re[n]

    def numTrees_2(self, n:int)->int:
        """
        直接利用数学公式，一个有n个节点的二叉树，一共有：
        (2n)!/((n+1)!*n!)
        :param n:
        :return:
        """
        return math.factorial(2*n)//(math.factorial(n+1)*math.factorial(n))


sol = Solution()
print(sol.numTrees_2(5))





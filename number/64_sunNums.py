# leetcode 64 中等
# 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
# 注意除法不可以用，因此无法用1+n除以2balabala的方法，不能用for，while不能用循环的方法
# 因此只能用递归的方法


class Solution:
    def sumNums(self, n:int)->int:
        """
        利用递归的方法来进行运算，
        利用逻辑短路（and，如果左侧为false，不会计算右侧的表达式，直接返回左侧的结果)，终止递归
        :param n:
        :return:
        """
        return n != 0 and n + self.sumNums(n-1)


sol = Solution()
print(sol.sumNums(2))
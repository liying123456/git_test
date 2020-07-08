# leetcode 20 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#     左括号必须用相同类型的右括号闭合。
#     左括号必须以正确的顺序闭合。
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
# 输入: "()"
# 输出: true


class Solution:
    def isValid(self, s: str) -> bool:
        """
        栈先进后出
        遇到左括号就放入栈中，遇到右括号，就和栈中最新元素进行对比，如果不是一对返回false
        如果栈为空，且遇到的右括号，返回false
        如果遍历了所有元素之后，栈仍没有清空，即有不配对的左括号，则返回false
        :param s:
        :return:
        """
        li = []
        for c in s:
            if c in ['(', '{', '[']:
                li.append(c)
            elif c == ')' and (li == [] or li.pop() != '('):
                return False
            elif c == '}' and (li == [] or li.pop() != '{'):
                return False
            elif c == ']' and (li == [] or li.pop() != '['):
                return False
        if li:
            return False
        return True


sol = Solution()
ss = input()
print(sol.isValid(ss))



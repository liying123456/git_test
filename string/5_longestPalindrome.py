# leetcode_5 回文
# 最长的回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

class Solution:
    def longestPalindrom_1(self, s: str)->str:
        """
        滑动循环的方法，
        设置一个滑动窗口（从len(s)开始并递减）。
        滑动窗口遍历字符串，取到子串，并得到逆字符串，
        如果子串和逆子串相等，就是回文子串。
        简单容易记
        :param str:
        :return:
        """
        win_size = len(s)
        while True:
            index = 0
            while index + win_size <= len(s):
                little_str = s[index: index+win_size]
                inverse_str = little_str[::-1]
                if little_str == inverse_str:
                    return little_str
                index = index + 1
            win_size = win_size - 1

    def longestPalindrom_2(self, s:str)->str:
        """
        动态规划
        从头到尾扫描字符串，字符i,
        然后判断以字符i结尾，且长度是maxlen+1和maxlen+2的子串是不是回文(+1和+2是奇数串和偶数串）
        如果是，更新最大回文子串。
        maxlen表示当前最大回文串的长度
        start表示回文开始的位置，start=i-maxlen或i-maxlen-1
        注意 s[0:3], 输出的是s0,s1,s2
        :param s:
        :return:
        """
        max_len = 0
        start = 0
        for i in range(len(s)):
            if i - max_len >= 1 and s[i-max_len-1: i+1] == s[i-max_len-1: i+1][::-1]:
                start = i - max_len - 1
                max_len = max_len + 2
                continue
            if i - max_len >= 0 and s[i-max_len: i+1] == s[i-max_len: i+1][::-1]:
                start = i - max_len
                max_len = max_len + 1
        return s[start: start+max_len]


sol = Solution()
print(sol.longestPalindrom_2('abcddc'))
print(sol.longestPalindrom_2('cbbd'))

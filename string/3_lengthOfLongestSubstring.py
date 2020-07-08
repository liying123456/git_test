# leetcode_3 string
# 无重复的最长字符子串


def lengthOfLongestSubstring_1(s):
    """
    hash
    :param s:
    :return:
    """
    dct = {}
    start = 0
    maxlength = 0
    for index, value in enumerate(s):
        if value in dct and start <= dct[value]:
            start = dct[value] + 1
        else:
            maxlength = max(maxlength, index - start + 1)
        dct[value] = index
    return maxlength


if __name__ == '__main__':
    s1 = 'abcabcbb'
    s2 = 'bbbbb'
    print(lengthOfLongestSubstring_1(s1))
    print(lengthOfLongestSubstring_1(s2))
# leetcode_1 数字计算
# 两数之和


def twoSum(nums, target):
    """
    hash
    :param nums:
    :param target:
    :return:
    """
    dct = {}
    for i in range(len(nums)):
        tmp = target - nums[i]
        if nums[i] not in dct:
            dct[tmp] = i
        else:
            return [dct[nums[i]], i]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))
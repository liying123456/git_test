# leetcode_287  字符串
# 寻找重复数
# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，
# 找出这个重复的数。



def findDuplicate_1(nums):
    """
    直接计数
    :param nums:
    :return:
    """
    for i in nums:
        if nums.count(i) > 1:
            return i


def findDuplicate_2(nums):
    """
    数学的方法，多余*c 除以 多余
    :param nums:
    :return:
    """
    set_nums = set(nums)
    result = (sum(nums) - sum(set_nums)) / (len(nums) - len(set_nums))
    return result


def findDuplicate_3(nums):
    """
    二分查找
    :param nums:
    :return:
    """
    left = 1
    right = len(nums) - 1
    while left < right:
        mid = int(left + (right - left) / 2)
        count = 0
        for num in nums:
            if num <= mid:
                count = count + 1
        if count <= mid:
            left = mid + 1
        else:
            right = mid
    return left


def findDuplicate_4(nums):
    """
    快慢指针
    :param nums:
    :return:
    """
    fast, slow = 0, 0
    while True:
        fast = nums[nums[fast]]
        slow = nums[slow]
        if fast == slow:  # prove there is a loop
            fast = 0  # important
            while nums[slow] != nums[fast]:  # find the duplicate
                fast = nums[fast]
                slow = nums[slow]
            return nums[fast]


if __name__ == '__main__':
    lis = [1, 3, 4, 2, 2]
    print(findDuplicate_4(lis))
    lis_2 = [3, 1, 3, 4, 2]
    print(findDuplicate_4(lis_2))

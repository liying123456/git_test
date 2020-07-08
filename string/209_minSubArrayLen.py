# leetcode 209 长度最小的子数组

# 与718类似,与287类似

# 给定一个含有n个正整数的数组和一个正整数s ，找出该数组中满足其和 ≥ s的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续
# 子数组，返回0。

# 示例：
# 输入：s = 7, nums = [2, 3, 1, 2, 4, 3]
# 输出：2
# 解释：子数组[4, 3]是该条件下的长度最小的连续子数组。

class Solution:
    def minSubArrayLen(self, s:int, nums:[int])->int:
        """
        二分查找法  o(nlogn)
        将原数组分为两部分，0~mid作为一个窗口大小，遍历整个数组，
        如果一旦满足，窗口内的和>=s，则将mid-1作为右边界，形成新的mid窗口，进行遍历
        如果窗口内



        :param s:
        :param nums:
        :return:
        """
        left = 1
        right = len(nums)
        result = 0
        while left <= right:
            mid = left + (right-left)//2
            tmp = self.windowex(nums, mid, s)
            if tmp:  # 该窗口的和可以>s，满足条件，则将该窗口作为总窗口，然后对半折叠
                right = mid - 1
                result = mid
            else:  # 该窗口内的和不满足条件，则将另外一边的窗口对折
                left = mid + 1
        return result

    def windowex(self, nums, size, s):
        """
        判断在窗口中，是否和>s
        :param nums:
        :param size:
        :param s:
        :return:
        """
        sumnum = 0
        for i in range(len(nums)):
            if i >= size:  # 右边的窗口作为总窗口, num[i-size]表示之前窗口中的第一个数
                sumnum = sumnum - nums[i - size]  # 去掉就窗口的第一个数，然后在接下来sum+num[i]这里添加一个新数，窗口长度始终为size大小
            sumnum = sumnum + nums[i]
            if sumnum >= s:
                return True
        return False


sol = Solution()
s = 7
nums = [1,4,4]
nums1 = [2, 3, 1, 2, 4, 3]
print(sol.minSubArrayLen(s,nums1))

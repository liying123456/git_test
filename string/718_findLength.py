# leetcode 718 最长重复子数组
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
#
# 示例 1:
# 输入:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出: 3
# 解释:
# 长度最长的公共子数组是 [3, 2, 1]。
#
# 说明:
#     1 <= len(A), len(B) <= 1000
#     0 <= A[i], B[i] < 100


class Solution:
    def findLength(self, A: [int], B: [int])->int:
        """
        动态规划, 维护一个公共子串长度表DP
        DP[i][j]表示A中以第i个元素，B中以第j个元素结尾的公共子串长度
        如果A[i]==B[j], DP[i][j]=DP[i-1][j-1]+1
        如果A[i]==B[j], DP[i][j]=0
        时间复杂度为：O（mn）
        :param A:
        :param B:
        :return:
        """
        na = len(A)
        nb = len(B)
        # na行，nb列的矩阵
        dp = [[0 for _ in range(nb)] for _ in range(na)]
        for i in range(na):
            for j in range(nb):
                if A[i] == B[j]:
                    if i >= 1 and j >= 1:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = 0
        max_length = max(max(row) for row in dp)
        return max_length


sol = Solution()
la = [0,0,0,0,1]
lb = [1,0,0,0,0]
print(sol.findLength(la, lb))
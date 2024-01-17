from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1]*(len(nums) + 1)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], res[j] + 1)
        print(res)
        return max(res)


print(Solution().lengthOfLIS(
    [1, 3, 6, 7, 9, 4, 10, 5, 6]
))

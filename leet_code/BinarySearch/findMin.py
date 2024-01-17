
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        mid = 0
        if nums[left] < nums[right]:
            return nums[left]
        while left < right:
            mid = (left+right)//2
            if nums[mid] >= nums[0]:
                left = mid + 1
            elif nums[mid] <= nums[-1]:
                right = mid
        return nums[left]


print(Solution().findMin(
    [2, 1]
))

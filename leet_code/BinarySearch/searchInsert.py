from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                right -= 1
        print(left)
        return left if target <= nums[-1] else left + 1


print(Solution().searchInsert(
    [1,3,5],
    3
))

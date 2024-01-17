from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_range, right_range = -1, -1
        if not nums:
            return [left_range, right_range]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                if mid > 0 and nums[mid] == nums[mid - 1]:
                    right = mid
                else:
                    left_range = mid
                    break
        if nums[left] == target:
            left_range = left
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                if mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                    left = mid + 1
                else:
                    right_range = mid
                    break
        if nums[0] == target:
            left_range = 0
        if nums[-1] == target:
            right_range = len(nums) - 1
        return [left_range, right_range]


print(Solution().searchRange(
    [1, 8],
    8
))

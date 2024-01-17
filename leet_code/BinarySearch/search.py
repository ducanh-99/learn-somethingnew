from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        mid = 0
        while left < right:
            mid = (left+right)//2
            if nums[mid] >= nums[0]:
                left = mid + 1
            elif nums[mid] <= nums[-1]:
                right = mid
        res = -1
        source_mid = mid
        left, right = 0, mid
        while left < right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                res = mid
                break
        left, right = source_mid, len(nums) - 1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                res = mid
                break
        return res
a = [1,2,3,4]
print(a.index(5))

print(Solution().search(
    [3, 1],
    3
))

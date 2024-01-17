from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        left, right = 0, len(nums1)
        n, m = len(nums1), len(nums2)
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (n + m + 1) // 2 - partition1
            maxLeft1 = float(
                "-inf") if partition1 == 0 else nums1[partition1-1]
            minRight1 = float("inf") if partition1 == n else nums1[partition1]
            maxLeft2 = float(
                "-inf") if partition2 == 0 else nums2[partition2-1]
            minRight2 = float("inf") if partition2 == m else nums2[partition2]
            print(maxLeft1, maxLeft2, minRight1, minRight2)
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (n + m) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)

            if maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1


print(Solution().findMedianSortedArrays(
    [1, 3],
    [2]
))

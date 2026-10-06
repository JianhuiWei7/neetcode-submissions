from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        # 1. 找最小值的位置
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        pivot = left

        # 2. 选择目标可能所在的有序区间
        if nums[pivot] <= target <= nums[-1]:
            left = pivot
            right = len(nums) - 1
        else:
            left = 0
            right = pivot - 1

        # 3. 普通二分查找
        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1
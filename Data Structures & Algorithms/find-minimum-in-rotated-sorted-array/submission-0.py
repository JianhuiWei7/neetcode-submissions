class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            midd = left + (right - left) // 2
            if nums[midd] > nums[right]:
                left = midd + 1
            elif nums[midd] < nums[right]:
                right = midd
        return nums[left]
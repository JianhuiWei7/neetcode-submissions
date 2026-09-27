class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for index, num in enumerate(nums):
            if index <= max_reach:
                max_reach = max(max_reach, num + index)
        if max_reach >= len(nums)-1:
            return True
        else:
            return False
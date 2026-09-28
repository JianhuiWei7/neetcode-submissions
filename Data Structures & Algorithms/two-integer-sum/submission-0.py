class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return [seen[remaining], index]
            else:
                seen[num] = index
        return 
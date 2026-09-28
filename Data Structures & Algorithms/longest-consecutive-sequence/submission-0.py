class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1
                while True:
                    if num + 1 in nums_set:
                        length += 1
                        num += 1
                    else:
                        break
                max_len = max(max_len, length)
        return max_len
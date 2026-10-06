class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def max_rob(nums):
            if len(nums) == 1:
                return nums[0]

            max_rob_list = [0] * (len(nums))
            max_rob_list[0] = nums[0]
            max_rob_list[1] = max(nums[1], nums[0])
            for i in range(2, len(nums)):
                max_rob_list[i] = max(max_rob_list[i-2] + nums[i], max_rob_list[i-1])
            return max_rob_list[-1]
        return max(max_rob(nums[1:]), max_rob(nums[0:-1]))
            


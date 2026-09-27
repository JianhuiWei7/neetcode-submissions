class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = [nums[0]] * len(nums)
        min_product = [nums[0]] * len(nums)
        answer = nums[0]
        for i in range(1, len(nums)):
            a = max_product[i-1] * nums[i]
            b = min_product[i-1] * nums[i]
            max_product[i] = max(a,b,nums[i])
            min_product[i] = min(a,b,nums[i])
            answer = max(answer, max_product[i])
        return answer
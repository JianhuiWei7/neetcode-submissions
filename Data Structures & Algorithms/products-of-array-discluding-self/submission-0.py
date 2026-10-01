class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_product = [1 for _ in range(len(nums))]
        current_product = 1
        for i in range(len(nums)):
            forward_product[i] = current_product
            current_product *= nums[i]
        backward_product = 1
        return_list = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            index = len(nums) - 1 - i
            return_list[index] = forward_product[index] * backward_product
            backward_product *= nums[index]
        return return_list

        

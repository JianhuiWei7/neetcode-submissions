class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return_list = [[]]
        def backtrack(lis, start_index):
            for i, num in enumerate(nums[start_index:]):
                lis.append(num)
                return_list.append(lis.copy())
                backtrack(lis, start_index + i + 1)
                lis.pop()
        backtrack([], 0)
        return return_list
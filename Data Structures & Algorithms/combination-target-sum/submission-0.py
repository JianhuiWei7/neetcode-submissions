class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        return_list = []
        current_list = []
        def backtrack(path, start, remaining):
            for i in range(start, len(nums)):
                if nums[i] == remaining:
                    path.append(nums[i])
                    return_list.append(path.copy())
                    path.pop()
                    return
                elif nums[i] > remaining:
                    return
                else:
                    path.append(nums[i])
                    backtrack(path, i, remaining - nums[i])
                    path.pop()

                
        backtrack([], 0,target)
        return return_list
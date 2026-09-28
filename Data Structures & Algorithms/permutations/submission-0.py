class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        return_list = []
        def backtrack(path):
            if len(path) == len(nums):
                return_list.append(path.copy())
                return
            for num in nums:
                if num not in used:
                    path.append(num)
                    used.add(num)

                    backtrack(path)
                    
                    path.pop()
                    used.remove(num)
        backtrack([])
        return return_list
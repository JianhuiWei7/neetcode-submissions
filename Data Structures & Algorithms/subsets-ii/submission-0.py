class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []

        def backtrack(start):
            result.append(path.copy())  # 当前路径本身就是一个子集

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result
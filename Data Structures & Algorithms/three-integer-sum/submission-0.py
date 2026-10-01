class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_res = set()
        for i in range(len(nums)):
            target = -nums[i]
            seen = set()
            for j in range(i+1, len(nums)):
                remaining = target - nums[j]
                if remaining in seen:
                    return_res.add(tuple(sorted([nums[i], remaining, nums[j]])))
                    # return_res.append([nums[i], remaining, nums[j]])
                seen.add(nums[j])
        
        return [list(triplet) for triplet in return_res]
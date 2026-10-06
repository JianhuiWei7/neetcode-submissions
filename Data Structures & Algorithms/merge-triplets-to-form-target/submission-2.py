class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        starting_index = -1
        for index, triplet in enumerate(triplets):
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                current_tripelt = triplet
                starting_index = index
                break
        if starting_index == -1:
            return False
        if current_tripelt[0] == target[0] and current_tripelt[1] == target[1] and current_tripelt[2] == target[2]:
            return True
        for index, triplet in enumerate(triplets[starting_index+1:]):
            new_0 = max(triplet[0],current_tripelt[0])
            new_1 = max(triplet[1],current_tripelt[1])
            new_2 = max(triplet[2],current_tripelt[2])
            if new_0 > target[0] or new_1 > target[1] or new_2 > target[2]:
                continue
            if new_0 == target[0] and new_1 == target[1] and new_2 == target[2]:
                return True
            current_tripelt = [new_0, new_1, new_2]
        return False

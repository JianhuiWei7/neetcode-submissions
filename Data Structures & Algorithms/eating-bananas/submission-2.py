class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            midd = left + (right - left) // 2
            h_needed = 0
            for pile in piles:
                h_needed += pile // midd
                if pile % midd != 0:
                    h_needed += 1
            if h_needed <= h:
                right = midd
            else:
                left = midd + 1
        return left
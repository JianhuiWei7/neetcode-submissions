from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for start in sorted(count):
            if count[start] == 0:
                continue

            # 有多少张 start，就必须组成多少组以 start 开头的牌
            groups = count[start]

            for val in range(start, start + groupSize):
                if count[val] < groups:
                    return False
                count[val] -= groups

        return True
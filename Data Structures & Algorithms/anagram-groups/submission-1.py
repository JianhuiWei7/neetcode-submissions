from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            counts = [0] * 26

            for char in s:
                counts[ord(char) - ord("a")] += 1

            # list 不可哈希，转成 tuple 作为字典的 key
            groups[tuple(counts)].append(s)

        return list(groups.values())
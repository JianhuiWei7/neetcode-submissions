class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 1
        left = 0
        right = 0
        current_set = set()
        if len(s) == 0:
            return 0
        current_set.add(s[right])
        while left < len(s)-1 and right < len(s)-1:
            if s[right + 1] not in current_set:
                right += 1
                current_set.add(s[right])
                max_len = max(max_len, len(current_set))
            else:
                current_set.remove(s[left])
                left += 1
        return max_len


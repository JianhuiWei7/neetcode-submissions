class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        current_char = {}
        left = 0
        right = 0
        max_len = 0
        while right<len(s):
            if s[right] in current_char:
                current_char[s[right]] += 1
            else:
                current_char[s[right]] = 1
            while right - left + 1 - max(current_char.values()) > k:
                current_char[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len

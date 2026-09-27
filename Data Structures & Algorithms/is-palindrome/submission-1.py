class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while not s[left].isalnum():
                if left + 1 >= len(s):
                    break
                else:
                    left += 1
            while not s[right].isalnum():
                if right - 1 < 0:
                    break
                else:
                    right -= 1
            if left >= right:
                return True
            else:
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                    continue
                else:
                    return False
        return True
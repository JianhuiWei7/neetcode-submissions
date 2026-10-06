class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        def expand(left,right):
            count = 0
            while s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
                if left < 0 or right == len(s):
                    break
            return count
        for i in range(len(s)):
            total += expand(i,i)
            if i + 1 != len(s):
                total += expand(i,i+1)
        return total
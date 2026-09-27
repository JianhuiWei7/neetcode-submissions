class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find_palindromic(index):
            str1 = None
            if index + 1 < len(s) and s[index] == s[index+1]:
                left = index
                right = index + 1
                while left > 0 and right + 1 < len(s):
                    if s[left-1] == s[right+1]:
                        left -= 1
                        right += 1
                    else:
                        break
                str1 = s[left:right+1]
            
            left = index
            right = index
            while left > 0 and right + 1 < len(s):
                if s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
                else:
                    break
            str2 = s[left:right+1]
            if str1 and len(str2) < len(str1):
                return str1
            return str2

        max_string = ""
        for index in range(len(s)):
            string1 = find_palindromic(index)
            if len(string1) >= len(max_string):
                max_string = string1
            else:
                continue
        return max_string



class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        left = {"[", "{", "("}
        stack = []
        for char in s:
            if char in left:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] == paren_dict[char]:
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0

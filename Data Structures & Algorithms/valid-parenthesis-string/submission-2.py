class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []
        for index, char in enumerate(s):
            if char == "(":
                left_stack.append(index)
            elif char == "*":
                star_stack.append(index)
            else:
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        while left_stack and star_stack:
            left_index = left_stack.pop()
            star_index = star_stack.pop()
            if star_index < left_index:
                return False
        return len(left_stack) == 0


                
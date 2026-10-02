from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            else:
                # 整数除法向零截断，例如 -13 / 5 = -2
                result = abs(left) // abs(right)
                if (left < 0) != (right < 0):
                    result = -result

            stack.append(result)

        return stack[0]
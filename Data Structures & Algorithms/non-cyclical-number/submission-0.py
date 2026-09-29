class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def convert_digit(n):
            sum_of_squares = 0
            while n > 0:
                digit = n % 10
                sum_of_squares += digit ** 2
                n = n // 10
            return sum_of_squares
        while True:
            n = convert_digit(n)
            if n == 1:
                return True
            elif n not in seen:
                seen.add(n)
            elif n in seen:
                return False
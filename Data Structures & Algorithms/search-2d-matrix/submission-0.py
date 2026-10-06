from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        def index2space(index):
            return index // cols, index % cols

        left = 0
        right = rows * cols - 1

        while left <= right:
            middle = left + (right - left) // 2
            x, y = index2space(middle)
            value = matrix[x][y]

            if value == target:
                return True
            elif value > target:
                right = middle - 1
            else:
                left = middle + 1

        return False
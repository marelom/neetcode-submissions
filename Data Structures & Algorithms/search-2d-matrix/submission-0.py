class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in range(len(matrix)):
            thing = matrix[x]
            for y in range(len(thing)):
                cell = matrix[x][y]
                if cell == target:
                    return True

        return False            
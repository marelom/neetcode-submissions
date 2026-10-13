class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        thing = len(matrix[0])
        for x in range(len(matrix)):
            for y in range(thing):
                cell = matrix[x][y]
                if cell == target:
                    return True

        return False            
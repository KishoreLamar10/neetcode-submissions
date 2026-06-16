class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        self.result =  [[0] * (cols + 1) for _ in range(rows + 1 )]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.result[r][c+1]
                self.result[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        row1, col1, row2, col2 = row1+1, col1 + 1, row2 + 1, col2 + 1
        bottomright = self.result[row2][col2]
        above = self.result[row1 - 1][col2]
        left = self.result[row2][col1-1]
        topleft = self.result[row1-1][col1-1]

        return bottomright - above - left + topleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
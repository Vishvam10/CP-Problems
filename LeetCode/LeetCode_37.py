class Solution:
    def solveSudoku(self, mat: List[List[str]]) -> None:
      """
      Do not return anything, modify board in-place instead.
      """

      def pp(mat) :
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in mat]))

      def isValid(mat, row, col, val):
        for i in range(9):
          if(mat[i][col] == val or mat[row][i] == val):
            return False

          ri = 3 * (row // 3) + i // 3
          ci = 3 * (col // 3) + i % 3
          if mat[ri][ci] == val:
              return False
        return True

      def solve(mat):
          for row in range(9):
              for col in range(9):
                  if mat[row][col] == ".":
                      for val in '123456789':
                          check = isValid(mat, row, col, val)
                          if check :
                          
                            # Set the state
                            mat[row][col] = val
                            
                            # Goto next state
                            res = solve(mat)

                            if res:
                              # If the next state can be solved
                              return True
                            else:
                              # Reset the state
                              mat[row][col] = "."

                      # No values exists for that square
                      return False
          
          # Solution found
          return True

      solve(mat)
      # pp(mat)
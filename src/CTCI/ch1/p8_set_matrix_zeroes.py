import unittest


def set_matrix_zeroes(matrix: list[list[int]]) -> list[list[int]]:
  if not matrix:
    return []
  
  # Time: O(m * n)
  # Space: O(m + n)
  def hash_table(matrix):
    
    zero_r = set()
    zero_c = set()
    for i in range(m):
      for j in range(n):
        if matrix[i][j] == 0:
          zero_r.add(i)
          zero_c.add(j)
        
    for i in range(m):
      for j in range(n):
        if i in zero_r or j in zero_c:
          matrix[i][j] = 0

    return matrix

  # Time: O(m*n)
  # Space: O(1)
  def mark_index(matrix):
    row = 0 in matrix[0]
    column = 0 in [r[0] for r in matrix]
    for i in range(1,m):
      for j in range(1, n):
        if matrix[i][j] == 0:
          matrix[i][0] = 0
          matrix[0][j] = 0

    for i in range(1,m):
      for j in range(1,n):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
          matrix[i][j] = 0        
    
    if column:
      for i in range(m):
        matrix[i][0] = 0
    
    if row:
      for j in range(n):
        matrix[0][j] = 0
    
    return matrix
  
  m, n = len(matrix), len(matrix[0])

  return mark_index(matrix)


class Test(unittest.TestCase):
  def test1(self):
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    output = [[1,0,1],[0,0,0],[1,0,1]]
    self.assertEqual(output,set_matrix_zeroes(matrix))

  def test2(self):
    matrix = [[0,1,1],[1,1,1],[1,1,1],[1,1,0]]
    output = [[0,0,0],[0,1,0],[0,1,0],[0,0,0]]
    self.assertEqual(output, set_matrix_zeroes(matrix))

  def test3(self):
    matrix = [[0,1,0],[1,1,1],[1,1,0]]
    output = [[0,0,0],[0,1,0],[0,0,0]]
    self.assertEqual(output, set_matrix_zeroes(matrix))

  def test4(self):
    self.assertEqual([[1]], set_matrix_zeroes([[1]]))
    self.assertEqual([[0,0]], set_matrix_zeroes([[1,0]]))
    self.assertEqual([[0]], set_matrix_zeroes([[0]]))
    self.assertEqual([[0],[0]], set_matrix_zeroes([[1],[0]]) )
    self.assertEqual([], set_matrix_zeroes([]))

    
if __name__ == '__main__':
  unittest.main()